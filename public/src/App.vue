<template>
  <div class="container">
    <Header
      :basket="basket"
      :username="username"
      :is-authenticated="!!username"
      @increment="incrementCount"
      @decrement="decrementCount"
      @clearBasket="clearBasket"
      @logout="handleLogout"
    />


    <RouterView
      :basket="basket"
      :addToBasket="addToBasket"
      :deleteFromBasket="deleteFromBasket"
      @increment="incrementCount"
      @decrement="decrementCount"
      @clearBasket="clearBasket"  
      @removeItem="removeCompletely"
    />

    <div v-if="showCookieNotice" class="cookie-notice">
      <p>
        🍪 Ми використовуємо cookie для збереження профілю та кошика.
        <button @click="acceptCookies">OK</button>
      </p>
    </div>

    <div v-if="basketMessage" class="basket-message">
      {{ basketMessage }}
    </div>
  </div>
</template>

<script>
import { RouterView } from 'vue-router';
import Header from './components/Header.vue';
import { useToast } from 'vue-toastification';

export default {
  components: { Header },
  data() {
    return {
      basket: [],
      username: "",
      showCookieNotice: false,
      basketMessage: '',
      basketTimeout: null,
      toast: useToast()
    };
  },
  methods: {
    getStorageKey() {
      return this.username ? `basket_user_${this.username}` : "basket_guest";
    },
    loadBasket() {
      const storedBasket = localStorage.getItem(this.getStorageKey());
      try {
        if (!storedBasket) {
          this.basket = [];
          return;
        }
        const basketData = JSON.parse(storedBasket);
        const now = Date.now();
        if (!this.username && now - basketData.timestamp > 1800000) {
          localStorage.removeItem(this.getStorageKey());
          this.basket = [];
        } else {
          this.basket = (basketData.items || []).map(item => ({ ...item, count: item.count || 1 }));
        }
      } catch (err) {
        console.warn("Помилка при зчитуванні кошика:", err);
        this.basket = [];
      }
    },
    saveBasket() {
      const basketData = { items: this.basket, timestamp: Date.now() };
      localStorage.setItem(this.getStorageKey(), JSON.stringify(basketData));
    },
    addToBasket(item) {
      const existing = this.basket.find(el => el.slug === item.slug);
      if (existing) {
        existing.count = (existing.count || 1) + 1;
      } else {
        this.basket.push({ ...item, count: 1 });
      }
      this.saveBasket();
      this.toast.success(`«${item.title}» додано до кошика!`);
    },
    deleteFromBasket(slug) {
      const item = this.basket.find(el => el.slug === slug);
      if (item) {
        item.count -= 1;
        if (item.count <= 0) {
          this.basket = this.basket.filter(el => el.slug !== slug);
        }
        this.saveBasket();
      }
    },
    removeCompletely(slug) {
      const removed = this.basket.find(item => item.slug === slug);
      this.basket = this.basket.filter(item => item.slug !== slug);

      localStorage.setItem(this.getStorageKey(), JSON.stringify({
        items: this.basket,
        timestamp: Date.now()
      }));

      if (removed) {
        this.toast.success(`«${removed.title}» видалено з кошика!`);
      }
    },
    incrementCount(slug) {
      const item = this.basket.find(el => el.slug === slug);
      if (item) {
        item.count += 1;
        this.saveBasket();
      }
    },
    decrementCount(slug) {
      const item = this.basket.find(el => el.slug === slug);
      if (item) {
        item.count -= 1;
        if (item.count <= 0) {
          this.basket = this.basket.filter(el => el.slug !== slug);
        }
        this.saveBasket();
      }
    },
    clearBasket() {
      this.basket = [];
      localStorage.removeItem(this.getStorageKey());
    },
    refreshUserBasket() {
      const newUsername = localStorage.getItem("username") || "";
      if (this.username !== newUsername) {
        this.username = newUsername;
        this.loadBasket(); 
      }
    },
    acceptCookies() {
      localStorage.setItem('cookiesAccepted', 'true');
      this.showCookieNotice = false;
    },
    async refreshTokenIfNeeded() {
      const token = localStorage.getItem("token");
      const refresh = localStorage.getItem("refresh");
      if (!token || !refresh) return;
      try {
        const res = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ refresh })
        });
        if (!res.ok) throw new Error("Refresh failed");
        const data = await res.json();
        localStorage.setItem("token", data.access);
      } catch {
        this.handleLogout();
      }
    },
    async checkAuth() {
      const token = localStorage.getItem("token");
      if (!token) return;
      try {
        const res = await fetch("http://127.0.0.1:8000/api/profile/", {
          headers: { Authorization: `Bearer ${token}` }
        });
        const data = await res.json();
        if (data.username) {
          localStorage.setItem("username", data.username);
          this.username = data.username;
          this.loadBasket();
        }
      } catch {
        this.handleLogout();
      }
    },
    handleLogout() {
      localStorage.removeItem("token");
      localStorage.removeItem("refresh");
      localStorage.removeItem("username");
      this.username = "";
      this.basket = [];
      window.dispatchEvent(new Event("storage"));
    }
  },
  created() {
    this.showCookieNotice = localStorage.getItem('cookiesAccepted') !== 'true';
    this.username = localStorage.getItem("username") || "";
    this.refreshTokenIfNeeded()
      .then(() => this.checkAuth())
      .then(() => this.loadBasket());
    window.addEventListener("storage", this.refreshUserBasket);
  },
  watch: {
    $route(to) {
      window.dispatchEvent(new Event("closeBasket"));
    },
    username() {
      this.loadBasket();
    }
  }
};
</script>

<style scoped>
.cookie-notice {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: #2f2f2f;
  color: #fff;
  padding: 16px 24px;
  text-align: center;
  font-size: 14px;
  line-height: 1.6;
  z-index: 1000;
  box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.3);
}

.cookie-notice strong {
  color: #00f7ff;
}

.cookie-notice button {
  margin-left: 10px;
  background: #00c896;
  border: none;
  padding: 6px 14px;
  color: white;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
}

.cookie-notice button:hover {
  background: #00ac82;
}

.basket-message {
  position: fixed;
  bottom: 70px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #00c896;
  color: white;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: bold;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  z-index: 1001;
  transition: opacity 0.3s ease;
}
</style>

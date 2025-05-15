<template>
  <header>
    <RouterLink to="/">
      <img src="/img/logo.svg" alt="Логотип" />
    </RouterLink>

    <button class="burger" @click="showMobileMenu = !showMobileMenu">☰</button>

    <ul>
      <li><RouterLink to="/">Головна</RouterLink></li>
      <li><RouterLink to="/items">Товари</RouterLink></li>
      <li><RouterLink to="/delivery">Доставка</RouterLink></li>
      <li><RouterLink to="/about">Про нас</RouterLink></li>

      <li class="basket-wrapper">
        <img src="/img/purchase.svg" @click="toggleBasket" alt="Кошик" />
        <div class="basket" v-if="showBasket && !isMobile" ref="basketRef">
          <div class="box"></div>
          <h3 v-if="basket.length === 0">Кошик порожній</h3>
          <div class="items" v-else>
            <div class="item" v-for="el in basket" :key="el.slug">
              <img :src="el.image" :alt="el.title">
              <div class="info">
                <h4>{{ el.title }} <small v-if="el.count > 1">×{{ el.count }}</small></h4>
                <p>{{ (el.price * el.count).toFixed(2) }}$</p>
                <div class="count-buttons">
                  <button @click="$emit('decrement', el.slug)">−</button>
                  <span>{{ el.count }}</span>
                  <button @click="$emit('increment', el.slug)">+</button>
                </div>
              </div>
            </div>
            <RouterLink to="/order">
              <button class="checkout-btn">Перейти до оплати</button>
            </RouterLink>
          </div>
        </div>
      </li>
    </ul>

    <div class="auth-buttons">
      <template v-if="!isAuthenticated">
        <RouterLink to="/login">Увійти</RouterLink>
        <RouterLink to="/register">Реєстрація</RouterLink>
      </template>
      <template v-else>
        <RouterLink to="/profile">Профіль ({{ username }})</RouterLink>
        <button @click="logout">Вийти</button>
      </template>
    </div>

    <div class="mobile-menu" v-if="showMobileMenu" ref="mobileMenuRef">
      <RouterLink to="/">Головна</RouterLink>
      <RouterLink to="/items">Товари</RouterLink>
      <RouterLink to="/delivery">Доставка</RouterLink>
      <RouterLink to="/about">Про нас</RouterLink>

      <div v-if="!isAuthenticated">
        <RouterLink to="/login">Увійти</RouterLink>
        <RouterLink to="/register">Реєстрація</RouterLink>
      </div>
      <div v-else>
        <RouterLink to="/profile">Профіль ({{ username }})</RouterLink>
        <button @click="logout">Вийти</button>
      </div>
    </div>

    <div
      v-if="basket.length && isMobile"
      ref="dragButton"
      class="mobile-cart-button"
      @click.stop="toggleBasket"
    >
      <img src="/img/purchase.svg" alt="Кошик" />
      <span class="badge">{{ basket.length }}</span>
    </div>

    <div
      class="basket"
      v-if="showBasket && isMobile"
      ref="basketRef"
      style="position: fixed; bottom: 80px; right: 16px; width: 90vw; z-index: 9999"
    >
      <div class="box"></div>
      <h3 v-if="basket.length === 0">Кошик порожній</h3>
      <div class="items" v-else>
        <div class="item" v-for="el in basket" :key="el.slug">
          <img :src="el.image" :alt="el.title">
          <div class="info">
            <h4>{{ el.title }} <small v-if="el.count > 1">×{{ el.count }}</small></h4>
            <p>{{ (el.price * el.count).toFixed(2) }}$</p>
            <div class="count-buttons">
              <button @click="$emit('decrement', el.slug)">−</button>
              <span>{{ el.count }}</span>
              <button @click="$emit('increment', el.slug)">+</button>
            </div>
          </div>
        </div>
        <RouterLink to="/order">
          <button class="checkout-btn">Перейти до оплати</button>
        </RouterLink>
      </div>
    </div>
  </header>
</template>

<script>
import { useToast } from 'vue-toastification';

export default {
  props: ['basket', 'username', 'isAuthenticated'],
  emits: ['clearBasket', 'decrement', 'increment', 'logout'],
  data() {
    return {
      showBasket: false,
      showMobileMenu: false,
      isMobile: false,
      toast: useToast()
    };
  },
  mounted() {
    this.checkIsMobile();
    window.addEventListener('resize', this.checkIsMobile);
    document.addEventListener("click", this.handleOutsideClick);

    const el = this.$refs.dragButton;
    if (el && this.isMobile) {
      this.enableDrag(el);
    }

    window.addEventListener("closeBasket", () => {
      this.showBasket = false;
    });

    this.$watch(
      () => this.$route.fullPath,
      () => {
        this.showMobileMenu = false;
      }
    );
  },

  beforeUnmount() {
    document.removeEventListener("click", this.handleOutsideClick);
    window.removeEventListener('resize', this.checkIsMobile);
  },
  methods: {
    toggleBasket() {
      this.showBasket = !this.showBasket;
    },
    checkIsMobile() {
      this.isMobile = window.innerWidth <= 768;
    },
    enableDrag(el) {
      el.onmousedown = (e) => {
        e.preventDefault();
        const shiftX = e.clientX - el.getBoundingClientRect().left;
        const shiftY = e.clientY - el.getBoundingClientRect().top;

        const moveAt = (pageX, pageY) => {
          el.style.left = pageX - shiftX + 'px';
          el.style.top = pageY - shiftY + 'px';
        };

        const onMouseMove = (e) => moveAt(e.pageX, e.pageY);

        document.addEventListener('mousemove', onMouseMove);

        document.onmouseup = () => {
          document.removeEventListener('mousemove', onMouseMove);
          document.onmouseup = null;
        };
      };
    },
    handleOutsideClick(event) {
      const basket = this.$refs.basketRef;
      const menu = this.$refs.mobileMenuRef;

      if (
        this.showBasket &&
        basket &&
        !basket.contains(event.target) &&
        !event.target.closest('.basket-wrapper') &&
        !event.target.closest('.mobile-cart-button')
      ) {
        this.showBasket = false;
      }

      if (
        this.showMobileMenu &&
        menu &&
        !menu.contains(event.target) &&
        !event.target.closest('.burger')
      ) {
        this.showMobileMenu = false;
      }
    },
    logout() {
      this.$emit("logout");
    }
  }
};
</script>



<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 30px 0;
  flex-wrap: wrap;
  background-color: #fff;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.05);
}
header img {
  height: 40px;
}
ul {
  list-style: none;
  display: flex;
  align-items: center;
  padding: 0;
  margin: 0;
}
ul li {
  margin: 0 15px;
  display: flex;
  align-items: center;
}
ul li a {
  font-size: 16px;
  color: black;
  text-decoration: none;
}
ul li img {
  width: 24px;
  height: 24px;
  cursor: pointer;
}
.auth-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}
.auth-buttons a,
.auth-buttons button {
  background: none;
  border: none;
  color: black;
  cursor: pointer;
  font-size: 15px;
  text-decoration: none;
}
.auth-buttons a:hover,
.auth-buttons button:hover,
ul li a:hover {
  color: #216f5b;
}
.basket-wrapper {
  position: relative;
}
.basket {
  position: absolute;
  top: 35px;
  right: 0;
  background: #f1f3f5;
  border-radius: 6px;
  padding: 15px;
  width: 280px;
  z-index: 100;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
}
.basket .box {
  position: absolute;
  top: -7px;
  right: 12px;
  width: 15px;
  height: 15px;
  transform: rotate(45deg);
  background: #f1f3f5;
}
.basket h3 {
  text-align: center;
  color: #616569;
  font-size: 16px;
}
.basket .item {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}
.basket .item img {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 4px;
}
.basket .item .info {
  flex-grow: 1;
}
.basket .item .info h4 {
  font-size: 14px;
  margin: 0;
  color: #333;
}
.basket .item .info p {
  margin: 4px 0;
  color: #216E5B;
  font-weight: 600;
}
.checkout-btn {
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  border: none;
  background-color: #216E5B;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
.checkout-btn:hover {
  background-color: #134438;
}
.burger {
  display: none;
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
}
.mobile-menu {
  position: absolute;
  top: 80px;
  left: 0;
  width: 100%;
  background: #ffffff;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  z-index: 9999;
  animation: slideDown 0.2s ease-out;
}

.mobile-menu > div {
  display: flex;
  flex-direction: column;
  align-items: center; 
  width: 100%;
  gap: 10px;
}

.mobile-menu a,
.mobile-menu button {
  font-size: 16px;
  color: #222;
  background: none;
  border: none;
  text-align: center;
  padding: 10px 0;
  border-bottom: 1px solid #eee;
  transition: color 0.2s;
}

.mobile-menu a:hover,
.mobile-menu button:hover {
  color: #216e5b;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.count-buttons {
  display: flex;
  gap: 6px;
  align-items: center;
}
.count-buttons button {
  background: #216E5B;
  color: white;
  border: none;
  padding: 4px 8px;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}
.count-buttons button:hover {
  background: #134438;
}
.mobile-cart-button {
  position: fixed;
  bottom: 16px;
  right: 16px;
  width: 56px;
  height: 56px;
  background-color: #10b981;
  border-radius: 50%;
  display: none;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  z-index: 9999;
  cursor: pointer;
}
.mobile-cart-button:active {
  cursor: grabbing;
}
.mobile-cart-button img {
  width: 24px;
  height: 24px;
  pointer-events: none;
}
.badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background-color: #ef4444;
  color: white;
  font-size: 12px;
  font-weight: bold;
  padding: 2px 6px;
  border-radius: 9999px;
}

@media (min-width: 769px) {
  .mobile-cart-button {
    display: flex;
  }
}

@media (max-width: 768px) {
  ul, .auth-buttons {
    display: none;
  }
  .burger {
    display: block;
  }
  .basket {
    width: 90vw;
    top: 45px;
    right: 0;
    font-size: 14px;
  }
  .basket .box {
    right: 20px;
  }
  .mobile-cart-button {
    display: flex !important;
  }

  .basket {
    width: 90vw;
    font-size: 14px;
    padding: 12px;
    right: 10px;
    left: auto;
    top: auto;
    bottom: 80px;
    max-height: 80vh;
    overflow-y: auto;
  }

  .basket .item {
    flex-direction: row;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 14px;
  }

  .basket .item img {
    width: 60px;
    height: 60px;
  }

  .basket .item .info h4 {
    font-size: 15px;
  }

  .basket .item .info p {
    font-size: 14px;
  }

  .count-buttons button {
    padding: 4px 8px;
    font-size: 14px;
  }

  .checkout-btn {
    font-size: 15px;
    padding: 10px;
    margin-top: 15px;
  }
}

</style>
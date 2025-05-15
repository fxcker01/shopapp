<template>
  <div>
    <div class="profile">
      <h1>Профіль користувача</h1>

      <div v-if="user">
        <label><strong>Логін:</strong>
          <input v-model="form.username" type="text" />
        </label>
        <label><strong>Email:</strong>
          <input v-model="form.email" type="email" />
        </label>
        <label>
          <input v-model="form.discount_notifications" type="checkbox" />
          Хочу отримувати повідомлення про знижки
        </label>

        <button @click="saveProfile">Зберегти</button>
        <button @click="logout" class="logout">Вийти</button>
      </div>

      <p v-else class="error">Не вдалося завантажити профіль.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  props: ['basket'],
  data() {
    return {
      toast: useToast(),
      user: null,
      form: {
        username: '',
        email: '',
        discount_notifications: false
      },
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("token");
      if (!token) {
        this.$router.push("/login");
        return;
      }

      const response = await axios.get("http://127.0.0.1:8000/api/profile/", {
        headers: { Authorization: `Bearer ${token}` }
      });

      this.user = response.data;
      this.form = { ...response.data }; 
    } catch (error) {
      console.error("Помилка отримання профілю:", error);
      this.error = "Не вдалося завантажити профіль.";
    }
  },
  methods: {
    async saveProfile() {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.put("http://127.0.0.1:8000/api/profile/", this.form, {
          headers: { Authorization: `Bearer ${token}` }
        });

        this.toast.success("Профіль успішно оновлено");
        this.user = response.data.profile;
      } catch (error) {
        console.error("Помилка збереження:", error);
        this.toast.error("Не вдалося зберегти зміни");
      }
    },
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");

      const username = this.user?.username;
      if (username) {
        localStorage.removeItem(`basket_user_${username}`);
      } else {
        localStorage.removeItem("basket_guest");
      }

      this.$router.push("/login");
      location.reload();
    }
  }
};

</script>
  
<style scoped>
.profile {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  font-weight: 500;
  font-size: 40px;
  color: #222;
}

label {
  display: block;
  margin: 15px 0 5px;
  text-align: left;
  font-size: 15px;
  color: #333;
}

input[type="text"],
input[type="email"] {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1.5px solid #ccc;
  border-radius: 6px;
  font-size: 15px;
  box-sizing: border-box;
  transition: border 0.2s;
}

input:focus {
  border-color: #216e5b;
  outline: none;
}

input[type="checkbox"] {
  margin-right: 6px;
}

button {
  display: block;
  width: 100%;
  padding: 12px;
  margin-top: 15px;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:first-of-type {
  background: #216e5b;
  color: white;
}

button:first-of-type:hover {
  background: #134438;
}

.logout {
  background: #d9534f;
  color: white;
}

.logout:hover {
  background: #c9302c;
}

.error {
  color: #d32f2f;
  font-size: 14px;
  margin-top: 10px;
}

.toast {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: 500;
  color: white;
  z-index: 1000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  animation: fade-in-out 3s ease;
}

.toast-success {
  background-color: #216e5b;
}

.toast-error {
  background-color: #d9534f;
}

@keyframes fade-in-out {
  0% { opacity: 0; transform: translateY(-10px); }
  10% { opacity: 1; transform: translateY(0); }
  90% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(-10px); }
}

@media (max-width: 480px) {
  .profile {
    margin: 60px 15px;
    padding: 20px 15px;
  }

  h1 {
    font-size: 26px;
  }

  label {
    font-size: 14px;
  }

  input,
  button {
    font-size: 14px;
  }
}
</style>

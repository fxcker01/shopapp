<template>
  <div class="login">
    <h1>Вхід</h1>
    <form @submit.prevent="loginUser">
      <input type="text" v-model="username" placeholder="Логін" required />
      <input type="password" v-model="password" placeholder="Пароль" required />
      <button type="submit">Увійти</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { useToast } from "vue-toastification";

export default {
  setup() {
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    async loginUser() {
      try {
        const res = await axios.post("/api/login/", {
          username: this.username,
          password: this.password
        });

        const { access, refresh } = res.data.tokens;

        localStorage.setItem("token", access);
        localStorage.setItem("refresh", refresh);
        localStorage.setItem("username", this.username);

        window.dispatchEvent(new Event("storage"));

        this.toast.success("Вхід успішний!");
        this.$router.push("/profile");
      } catch (error) {
        console.error("Помилка входу:", error);
        const msg = error.response?.data?.error || "Невірний логін або пароль.";
        this.toast.error(msg);
      }
    }

  }
};
</script>

<style scoped>
.login {
  max-width: 360px;
  margin: 100px auto;
  padding: 20px;
  text-align: center;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

h1 {
  margin-bottom: 20px;
  font-weight: 500;
  font-size: 32px;
  color: #222;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

input {
  padding: 12px;
  border: 1.5px solid #ccc;
  border-radius: 6px;
  font-size: 15px;
  transition: border 0.2s;
}

input:focus {
  border-color: #216e5b;
  outline: none;
}

button {
  padding: 12px;
  background: #206e5b;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background: #134438;
}

@media (max-width: 480px) {
  .login {
    margin: 60px 15px;
    padding: 20px 15px;
  }

  h1 {
    font-size: 26px;
  }

  input, button {
    font-size: 15px;
  }
}
</style>


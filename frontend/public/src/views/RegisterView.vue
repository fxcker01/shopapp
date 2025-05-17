<template>
    <div class="register">
      <h1>Реєстрація</h1>
      <p class="error" v-if="error">{{ error }}</p>
      <form @submit.prevent="registerUser">
        <input type="text" v-model="username" placeholder="Логін" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Пароль" required />
        <button type="submit">Зареєструватися</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useToast } from 'vue-toastification';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        error: ''
      };
    },
    methods: {
      async registerUser() {
        this.error = '';
        const toast = useToast();

        try {
          const response = await axios.post("/api/register/", {
            username: this.username,
            email: this.email,
            password: this.password
          });

          const tokens = response.data.tokens;
          if (!tokens || !tokens.access || !tokens.refresh) {
            this.error = "Помилка сервера: відсутні токени!";
            toast.error(this.error);
            return;
          }

          localStorage.setItem("token", tokens.access);
          localStorage.setItem("refresh", tokens.refresh);
          localStorage.setItem("username", this.username);

          window.dispatchEvent(new Event("storage"));

          toast.success("Реєстрація успішна!");
          this.$router.push("/profile");

        } catch (error) {
          if (error.response) {
            if (error.response.data.error === "Користувач з таким логіном вже існує") {
              this.error = "Логін вже зайнятий! Виберіть інший.";
            } else {
              this.error = error.response.data?.error || "Помилка реєстрації. Спробуйте ще раз!";
            }
          } else {
            this.error = "Помилка сервера. Перевірте з'єднання.";
          }
          toast.error(this.error);
        }
      }


    }
  };
  </script>
  
  <style scoped>
  .register {
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
  
  .error {
    color: #d32f2f;
    margin-bottom: 10px;
    font-size: 14px;
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
    .register {
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
  



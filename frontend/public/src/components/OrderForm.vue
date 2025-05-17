<template>
  <div>
    <h1>Оформлення замовлення</h1>
    <div class="data">
      <div class="basket" v-if="basketItems.length > 0">
        <div class="item" v-for="el in basketItems" :key="el.slug">
          <img :src="el.image" :alt="el.title">
          <h3>{{ el.title }}</h3>

          <div class="info-wrapper">
            <span>{{ (el.price * (el.count || 1)).toFixed(2) }}$</span>
            <div class="count-buttons">
              <button @click="$emit('decrement', el.slug)">−</button>
              <span>{{ el.count || 1 }}</span>
              <button @click="$emit('increment', el.slug)">+</button>
            </div>
            <button @click="removeItem(el.slug)">Видалити</button>
          </div>
        </div>
        <span>Разом: {{ getSumma }}$</span>
      </div>
      <div v-else>
        <h2>Товарів немає</h2>
      </div>

      <form class="order-form" @submit.prevent="sendData">
        <input type="text" v-model="name" placeholder="Ваше ім'я">
        <input type="text" v-model="surname" placeholder="Ваше прізвище">
        <input type="email" v-model="email" placeholder="Ваш email">
        <input type="tel" v-model="phone" placeholder="Телефон">

        <label for="delivery">Спосіб доставки:</label>
        <select v-model="delivery_method" id="delivery">
          <option value="courier">Кур'єрська доставка</option>
          <option value="pickup">Самовивіз</option>
          <option value="post">Пошта</option>
        </select>

        <input v-if="delivery_method !== 'pickup'" type="text" v-model="address" placeholder="Ваша адреса">
        <button type="submit">Купити</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  props: ['basket', 'deleteFromBasket'],
  emits: ['increment', 'decrement', 'clearBasket', 'removeItem'],
  data() {
    return {
      name: '',
      surname: '',
      email: '',
      phone: '',
      delivery_method: 'courier',
      address: ''
    };
  },
  computed: {
    basketItems() {
      return Array.isArray(this.basket) ? this.basket : (this.basket.items || []);
    },
    getSumma() {
      return this.basketItems.reduce((total, item) => {
        const quantity = item.count || 1;
        return total + parseFloat(item.price) * quantity;
      }, 0).toFixed(2);
    }
  },
  methods: {
    removeItem(slug) {
      this.$emit('removeItem', slug);
    },
    async sendData() {
      const toast = useToast();

      if (this.name.length < 2) return toast.error('Імʼя повинно містити не менше 2 символів');
      if (this.surname.length < 2) return toast.error('Прізвище повинно містити не менше 2 символів');
      if (!this.email.includes('@') || !this.email.includes('.')) return toast.error('Email введено неправильно');
      if (this.phone.length < 10) return toast.error('Телефон повинен містити не менше 10 цифр');
      if (this.basketItems.length === 0 || this.getSumma === 0) return toast.error('Кошик порожній');

      try {
        const data = {
          name: this.name,
          surname: this.surname,
          email: this.email,
          phone: this.phone,
          summa: this.getSumma,
          basket: this.basketItems,
          delivery_method: this.delivery_method,
          address: this.address
        };

        const res = await axios.post("/api/order-add/", data, {
          headers: { "Content-Type": "application/json" }
        });

        toast.success(res.data.result || "Замовлення успішно оформлене!");

        this.name = '';
        this.surname = '';
        this.email = '';
        this.phone = '';
        this.delivery_method = 'courier';
        this.address = '';
        this.$emit('clearBasket');

        const key = localStorage.getItem("username")
          ? `basket_user_${localStorage.getItem("username")}`
          : "basket_guest";

        localStorage.setItem(key, JSON.stringify({
          items: [],
          timestamp: Date.now()
        }));
      } catch (error) {
        console.error("Помилка:", error.response?.data || error.message);
        toast.error("Помилка при відправці замовлення!");
      }
    }
  }
};
</script>

<style scoped>
.data {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  gap: 40px;
  margin: 50px auto;
  max-width: 1200px;
  padding: 0 20px;
  box-sizing: border-box;
}

.data > div {
  flex: 1 1 0px;
  max-width: 500px;
}

h1 {
  margin-top: 100px;
  font-weight: 400;
  font-size: 70px;
  text-align: center;
  font-size: 60px;
}

.basket {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  width: 100%;
  box-sizing: border-box;
}

.order-form {
  width: 100%;
  max-width: 500px;
  background: #fdfdfd;
  padding: 0 25px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  box-sizing: border-box;
}

.item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  padding-bottom: 20px;     
  border-bottom: 1px solid #ddd; 
  margin-bottom: 20px;
}

.item img {
  width: 60px;
  height: auto;
  object-fit: contain;
}

.item h3 {
  color: #52585c;
  font-size: 15px;
  flex: 1;
  margin: 0;
}

.info-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.item span {
  font-weight: 600;
  color: #323232;
}

.item button {
  border: 0;
  background: rgb(186, 43, 43);
  border-radius: 5px;
  padding: 7px 12px;
  cursor: pointer;
  color: #fff;
  transition: background 0.3s;
}

.item button:hover {
  background: rgb(133, 28, 28);
}

.basket > span {
  display: block;
  font-weight: 600;
  color: #206E5B;
  margin-top: 20px;
  font-size: 18px;
}

form input,
form select {
  width: 100%;
  padding: 10px;
  margin-bottom: 12px;
  border: 1.5px solid #575d61;
  border-radius: 5px;
  background: #fff;
  font-size: 15px;
  color: #333;
  outline: none;
  box-sizing: border-box;
}

form input:focus,
form select:focus {
  border-color: #242424;
}

form button {
  background: #206E5B;
  color: #fff;
  border: none;
  padding: 12px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  width: 100%;
  transition: background 0.3s ease;
}

form button:hover {
  background: #134438;
}

.count-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

.count-buttons button {
  background: #206E5B;
  color: white;
  border: none;
  padding: 4px 10px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.count-buttons button:hover {
  background: #134438;
}

.fade-enter-active, .fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}


@media (max-width: 768px) {
  h1 {
    font-size: 40px;
    margin-top: 60px;
  }

  .data {
    flex-direction: column;
    align-items: center;
    padding: 0 10px;
  }

  .data > div {
    max-width: 100%;
  }

  .item {
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
  }

  .item h3 {
    flex: 1 1 100%;
    font-size: 14px;
    margin-bottom: 5px;
  }

  .info-wrapper {
    display: flex;
    flex: 1 1 100%;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    flex-wrap: nowrap;
  }

  .info-wrapper button {
    white-space: nowrap;
  }

  .item img {
    max-width: 120px;
  }

  .order-form {
    padding: 20px;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 32px;
    margin-top: 40px;
  }

  .basket {
    padding: 15px;
  }

  .order-form {
    padding: 15px;
  }

  .item h3 {
    font-size: 14px;
  }

  .item span {
    font-size: 14px;
  }
}
</style>

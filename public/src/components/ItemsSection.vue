<template>
    <div class="items">
        <div class="item" v-for="el in items" :key="el.slug">
            <RouterLink :to="`/item/${el.slug}`" class="clickable">
                <img :src="el.image" :alt="el.title">
                <h3>{{ el.title }}</h3>
                <p class="item-desc">{{ el.desc }}</p>
            </RouterLink>
            <div class="bottom">
                <span>{{ el.price }}$</span>
                <img src="/img/add-to-basket.svg" :alt="el.title" @click="addToBasket(el)">
            </div>
        </div>
    </div>
    <div class="pagination">
      <button
        :disabled="currentPage === 1"
        @click="fetchItems(currentPage - 1)"
      >
        ← Назад
      </button>

      <button
        v-for="page in totalPages"
        :key="page"
        @click="fetchItems(page)"
        :class="{ active: page === currentPage }"
      >
        {{ page }}
      </button>

      <button
        :disabled="currentPage === totalPages"
        @click="fetchItems(currentPage + 1)"
      >
        Далі →
      </button>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    props: ['addToBasket'],
    data() {
        return {
          pageSize: 6,
          items: [],
          currentPage: 1,
          totalPages: 1,
        }
    },
    async mounted() {
      this.fetchItems(1);
    },
    methods: {
      async fetchItems(page = 1) {
        try {
          const res = await axios.get(`/api/items/?page=${page}`);
          this.items = res.data.results;
          this.totalPages = Math.ceil(res.data.count / this.pageSize);
          this.currentPage = page;
          window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch (error) {
          console.error('Помилка завантаження:', error);
        }
      },
      updateItemInList(updatedItem) {
        const index = this.items.findIndex(item => item.slug === updatedItem.slug);
        if (index !== -1) {
          this.items[index] = updatedItem;  
        }
      }
  }
};
</script>

<style scoped>
.items {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px 20px; 
  padding: 10px 3%;
  box-sizing: border-box;
}

.items .item {
  flex: 1 1 260px;     
  max-width: 300px;
  background: #F4F4F4;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  padding: 20px;
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.items .item:hover {
  transform: translateY(-5px);
}

.items .item img:first-child {
  width: 100%;
  height: 260px;
  object-fit: cover;
  border-radius: 6px;
}

.items .item h3 {
  margin: 12px 0 6px;
  font-size: 20px;
  color: #216E5B;
}

.items .item p {
  margin: 0 0 12px;
  font-size: 15px;
  color: #444;
}

.items .item .bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
}

.items .item .bottom span {
  font-weight: 600;
  color: #216E5B;
  font-size: 16px;
}

.items .item .bottom img {
  width: 24px;
  height: 24px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.items .item .bottom img:hover {
  transform: scale(1.3);
}

.item-desc {
  display: -webkit-box;
  -webkit-line-clamp: 1; 
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}

.pagination {
  margin: 10px 0;
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
}

.pagination button {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background: #eee;
  color: #333;
  cursor: pointer;
  transition: 0.2s;
}

.pagination button.active {
  background: #216E5B;
  color: white;
  font-weight: bold;
}

.pagination button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

@media (max-width: 480px) {
  .items .item {
    flex: 1 1 90%;
    padding: 14px;
  }

  .items .item h3 {
    font-size: 18px;
  }

  .items .item p {
    font-size: 14px;
  }

  .items .item img:first-child {
    height: 200px;
  }
}


</style>

<template>
  <div class="product-page" v-if="item">
    <div v-if="showZoom" class="zoom-overlay" @click.self="resetZoom">
      <div class="zoom-container" ref="zoomContainer">
        <img
          :src="activeImage"
          :alt="item.title"
          class="zoomed-image"
          ref="zoomedImage"
        />
      </div>
    </div>

    <div class="image-box">
      <img
        :src="activeImage"
        :alt="item.title"
        @click="openZoom"
        class="main-image"
      />
      <div class="thumbnails">
        <img
          v-for="(img, index) in item.images"
          :key="index"
          :src="img.image"
          :alt="item.title"
          :class="['thumbnail-image', { active: img.image === activeImage }]"
          @click="activeImage = img.image"
        />
      </div>
    </div>

    <div class="info-box">
      <h1>{{ item.title }}</h1>
      <p class="desc">{{ item.desc }}</p>
      <p class="price">{{ Number(item.price).toFixed(2) }} $</p>

      <div class="quantity-controls">
        <button @click="decrementCount">−</button>
        <div class="count-box">{{ count }}</div>
        <button @click="incrementCount">+</button>
      </div>

      <button @click="handleAddToBasket">Додати в кошик</button>
      <button class="go-basket" @click="$router.push('/order')">Перейти до кошика</button>
    </div>
  </div>
</template>



<script>
import axios from 'axios';
import Panzoom from '@panzoom/panzoom';

export default {
  props: ['addToBasket'],
  data() {
    return {
      item: null,
      activeImage: '',
      count: 1,
      showZoom: false,
      panzoomInstance: null,
    };
  },
  async mounted() {
    const slug = this.$route.params.slug;
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/item/${slug}/`);
      this.item = res.data;
      this.activeImage = res.data.image;

      if (!this.item.images || !this.item.images.length) {
        this.item.images = [this.item.image];
      }
    } catch (err) {
      console.error("Не вдалося завантажити товар:", err);
    }
  },
  methods: {
    incrementCount() {
      this.count++;
    },
    decrementCount() {
      if (this.count > 1) this.count--;
    },
    handleAddToBasket() {
      for (let i = 0; i < this.count; i++) {
        this.addToBasket(this.item);
      }
    },
    openZoom() {
      this.showZoom = true;
      this.$nextTick(() => {
        const image = this.$refs.zoomedImage;

        this.panzoomInstance = Panzoom(image, {
          maxScale: 5,
          minScale: 1,
          contain: 'outside',
        });

        image.addEventListener('wheel', this.panzoomInstance.zoomWithWheel);
      });
    },

    resetZoom() {
      const image = this.$refs.zoomedImage;
      if (this.panzoomInstance) {
        image.removeEventListener('wheel', this.panzoomInstance.zoomWithWheel);
        this.panzoomInstance.destroy();
        this.panzoomInstance = null;
      }
      this.showZoom = false;
    }
  }
};
</script>

<style scoped>
.product-page {
  display: flex;
  gap: 40px;
  max-width: 1000px;
  margin: 50px auto;
  padding: 20px;
  flex-wrap: wrap;
}

.main-image {
  width: 100%;
  max-width: 600px !important;
  min-width: 350px;
  height: auto;
  border-radius: 12px;
  cursor: pointer;
}

.thumbnails {
  display: flex;
  gap: 10px;
  margin-top: 10px;
  flex-wrap: wrap;
}

.thumbnail-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 6px;
  cursor: pointer;
  opacity: 0.7;
  transition: opacity 0.3s, border 0.3s;
}
.thumbnail-image.active,
.thumbnail-image:hover {
  opacity: 1;
  border: 2px solid #216E5B;
}
.info-box {
  flex: 1;
  min-width: 280px;
}
.info-box h1 {
  margin-top: 0px;
  font-size: 32px;
  margin-bottom: 10px;
}
.desc {
  margin-bottom: 15px;
  color: #444;
}
.price {
  font-size: 20px;
  color: #216E5B;
  font-weight: bold;
  margin-bottom: 20px;
}
.quantity-controls {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
}

.quantity-controls button:first-of-type {
  margin-right: 3px;
}


.quantity-controls button {
  background: #216E5B;
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  font-size: 20px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s;
}

.quantity-controls button:hover {
  background: #134438;
}

.count-box {
  min-width: 40px;
  height: 40px;
  background: #f3f3f3;
  border-radius: 4px;
  font-weight: bold;
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
button,
button.go-basket {
  background: #216E5B;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  display: inline-block;
  margin-bottom: 10px;
  margin-right: 10px; 
  width: auto;
  transition: background 0.3s ease, transform 0.2s ease;
}

button.go-basket {
  background: #444;
}

button:hover {
  background: #1b5d4d;
  transform: translateY(-2px);
}

button.go-basket:hover {
  background: #2a2a2a;
  transform: translateY(-2px);
}

.main-image {
  /* cursor: zoom-in; */
  cursor: pointer;
  border-radius: 8px;
}

.zoom-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;

  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  cursor: zoom-in;
}

.zoom-container {
  width: 50vw;
  height: 90vh;
  overflow: hidden;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  touch-action: none;
}

.zoomed-image {
  width: 100%;
  height: auto;
  user-select: none;
  cursor: grab;
  touch-action: none;
}


@media (max-width: 768px) {
  .product-page {
    flex-direction: column;
    align-items: center;
    padding: 10px;
  }
  .image-box img {
    max-width: 100%;
    max-height: 300px; 
  }
  .thumbnails img {
    width: 64px;
    height: 64px;
  }
  .info-box {
    width: 100%;
  }
  .info-box h1 {
    font-size: 24px;
    text-align: center;
  }
  .desc, .price {
    text-align: center;
  }
  .quantity-controls {
    justify-content: center;
  }
  button.go-basket {
    margin-left: 0;
    margin-top: 10px;
    width: 100%;
  }
  button,
  button.go-basket {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .zoom-container {
    width: 90vw;
    height: 50vh;
    padding: 0;
    margin: 0;
    border-radius: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    touch-action: none;
  }

  .zoomed-image {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    cursor: grab;
    touch-action: none;
  }
}


</style>
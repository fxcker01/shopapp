<template>
  <div class="delivery-page">
    <h1>Доставка</h1>
    <p>
      Ми доставляємо меблі по всій Україні швидко та зручно. 
      <br><br>
      Стандартний термін доставки — 1–5 робочих днів з моменту оформлення замовлення. 
      <br><br>
      Доставка здійснюється нашими кур'єрами або службами доставки (Нова Пошта, Meest).
      <br><br>
      Ви можете обрати зручний спосіб доставки під час оформлення замовлення.
    </p>
  </div>
</template>
  
  <script>
  export default {
    props: ['basket']
  }
  </script>
  
  <style scoped>
  .delivery-page {
    max-width: 800px;
    margin: 100px auto 40px;
    padding: 0 20px;
  }
  
  h1 {
    font-weight: 400;
    font-size: 60px;
    margin-bottom: 30px;
    text-align: center;
  }
  
  p {
    font-size: 18px;
    line-height: 1.6;
    color: #333;
    text-align: justify;
  }
  
  @media (max-width: 768px) {
    h1 {
      font-size: 42px;
    }
  
    p {
      font-size: 16px;
    }
  
    .delivery-page {
      margin-top: 60px;
      padding: 0 16px;
    }
  }
  </style>
  
<template>
  <div class="about-page">
    <h1>Про нас</h1>
    <p>
      Ми — команда, яка з любов’ю створює комфорт у вашому домі. Наш меблевий магазин пропонує сучасні, якісні та доступні меблі для будь-якого інтер’єру.
      <br><br>
      Ми працюємо безпосередньо з виробниками, тому гарантуємо високу якість і чесну ціну. У нашому асортименті ви знайдете все: від кухонних гарнітурів до зручних диванів і шаф.
      <br><br>
      Кожен клієнт для нас — важливий, тому ми надаємо індивідуальний підхід, швидку доставку та післяпродажне обслуговування.
      <br><br>
      Обираючи нас, ви обираєте комфорт, стиль і надійність.
    </p>
  </div>
</template>
  
  <script>
  export default {
    props: ['basket']
  }
  </script>
  
  <style scoped>
  .about-page {
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
  
  /* 📱 Mobile */
  @media (max-width: 768px) {
    h1 {
      font-size: 42px;
    }
  
    p {
      font-size: 16px;
    }
  
    .about-page {
      margin-top: 60px;
      padding: 0 16px;
    }
  }
  </style>
  
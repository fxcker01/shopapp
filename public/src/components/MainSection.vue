<template>
    <div class="wrapper">
        <img src="/img/main-image.svg" alt="">
        <div>
            <img src="/img/asterics.svg" alt="">
            <h1>Shop</h1>
            <h2>online</h2>
            <h3>now</h3>
            <p>Ми створюємо стиль і комфорт для вашого дому — обирайте якісні меблі з натуральних матеріалів, які доповнять будь-який інтер’єр.</p>
            <RouterLink to="/items"><button>Перейти до каталогу</button></RouterLink>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 100px;
}

.wrapper > div {
    margin-left: 50px;
    color: #373845;
}

.wrapper > div h1 {
    font-weight: 400;
    font-size: 90px;
    margin-top: 20px;
}

.wrapper > div h2, .wrapper > div h3 {
    font-weight: 400;
    font-size: 70px;
}

.wrapper > div h3 {color: #5CDDBC;}

.wrapper > div p {
    font-size: 18px;
    max-width: 500px;
    margin: 20px 0;
} 

.wrapper > div button {
    font-weight: 600;
    font-size: 18px;
    color: #2F323A;
    background: #5CDDBC;
    border-radius: 25px;
    border: 0;
    padding: 15px 25px;
    cursor: pointer;
}

.wrapper > div button:hover {
    transform: translateY(-5px);
}

@media (max-width: 1024px) {
  .wrapper {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 25px;
    padding: 0 30px;
  }

  .wrapper > div {
    margin-left: 0;
    width: 100%;
  }

  .wrapper > div img {
    display: none;
  }

  .wrapper img:first-child {
    width: 100%;
    max-width: 500px;
    height: auto;
    object-fit: contain;
  }

  .wrapper > div h1 {
    font-size: 70px;
    margin-top: 20px;
  }

  .wrapper > div h2,
  .wrapper > div h3 {
    font-size: 50px;
  }

  .wrapper > div p {
    font-size: 17px;
    margin: 20px 0;
    width: 100%;
  }

  .wrapper > div button {
    width: 100%;
    font-size: 16px;
    padding: 12px 20px;
  }
}


@media (max-width: 768px) {
  .wrapper {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
    padding: 0 10px;
  }

  .wrapper img:first-child {
    width: 100%;
    max-width: none;
    height: auto;
    object-fit: cover;
  }

  .wrapper > div {
    margin-left: 0;
    width: 100%;
  }

  .wrapper > div img {
    display: none;
  }

  .wrapper > div h1 {
    font-size: 64px;
    margin: 10px 0 0;
    word-break: break-word;
  }

  .wrapper > div h2,
  .wrapper > div h3 {
    font-size: 48px;
    margin: 0;
    word-break: break-word;
  }

  .wrapper > div p {
    font-size: 16px;
    width: 100%;
    margin: 20px 0;
  }

  .wrapper > div button {
    width: 100%;
    font-size: 16px;
    padding: 12px 20px;
  }
}
</style>
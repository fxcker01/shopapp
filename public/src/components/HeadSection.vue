<template>
    <div class="wrapper">
        <div>
            <h1>Наші меблі</h1>
            <h2>Стиль та комфорт для вашого дому</h2>
        </div>
        <div>
            <img src="/img/main-image.svg" alt="">
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    background: #5CDDBC;
    width: 100%;
    display: flex;
    padding: 0 5%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #216F5B;
    margin: 10px 0;
    flex-wrap: wrap;
    gap: 20px;
    box-sizing: border-box;
}

.wrapper h1 {
    margin: 0;
    font-size: 60px;
}

.wrapper h2 {
    font-size: 24px;
    font-weight: 400;
    margin-top: 10px;
}

.wrapper img {
    height: 200px;
    max-width: 100%;
    object-fit: contain;
    position: static;
}


@media (max-width: 768px) {
    .wrapper {
        flex-direction: column-reverse;
        text-align: center;
        height: auto;
        padding: 20px 5%;
    }

    .wrapper h1 {
        font-size: 40px;
    }

    .wrapper h2 {
        font-size: 18px;
    }

    .wrapper img {
        height: 180px;
    }
}
</style>
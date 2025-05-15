<script>
import HeadSection from '../components/HeadSection.vue'
import ItemsSection from '../components/ItemsSection.vue'

export default {
    props: ['basket', 'addToBasket'],
    components: { HeadSection, ItemsSection }
}
</script>

<template>
    <div>
        <HeadSection />
        <ItemsSection :addToBasket="addToBasket"/>
    </div>
</template>

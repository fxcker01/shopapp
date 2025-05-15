<script>
import OrderForm from '../components/OrderForm.vue'

export default {
    props: ['basket', 'deleteFromBasket'],
    emits: ['increment', 'decrement', 'clearBasket', 'removeItem'],
    components: { OrderForm }
}
</script>

<template>
    <div>
        <OrderForm
            :basket="basket"
            :deleteFromBasket="deleteFromBasket" 
            @clearBasket="$emit('clearBasket')"
            @increment="$emit('increment', $event)"
            @decrement="$emit('decrement', $event)"
            @removeItem="$emit('removeItem', $event)"
        />
    </div>
</template>

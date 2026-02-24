<!--Copy this boilerplate for easy component building-->
<script setup >import { defineProps } from 'vue';
const Props = defineProps(['text', 'author'])

</script>

<template>
    <div class="Quote-container">
        <span class="text">"{{ Props.text }}"</span>
        <span class="author">{{ Props.author }}</span>
    </div>

</template>

<style scoped>
.Quote-container{
    min-width: 120px;
    max-width: 250px;
    height: 200px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
   backdrop-filter: blur(50px);
     -webkit-backdrop-filter: blur(50px) ;
}
.text{
    font-size: 25px;
    font-style: italic;
}
</style>
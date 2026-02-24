<!--Copy this boilerplate for easy component building-->
<script setup >

const Props = defineProps(['propsrc'])
console.log(Props.propsrc)
</script>

<template>
    <img :src="Props.propsrc" alt=""/>
</template>

<style scoped>
img{
    width: 500px;
    height: auto;
    image-rendering: smooth;
}
</style>
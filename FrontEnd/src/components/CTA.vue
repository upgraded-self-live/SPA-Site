<!--Copy this boilerplate for easy component building-->
<script setup >
import CTAbutton from './CTAbutton.vue'
</script>

<template>
    <div class="full-background">
        <span class="title"></span>
        <CTAbutton/>
    </div>
</template>

<style scoped>
div{
    position: relative;
    top: 130px;
    width: 100%;
    display: flex;
    min-height: 130px;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}
.full-background{
    background-color: white;
}
.title {
  font-size: 60px;
  font-weight: 700;
}
</style>
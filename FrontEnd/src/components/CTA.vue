<!--Copy this boilerplate for easy component building-->
<script setup>
import CTAbutton from './CTAbutton.vue'
</script>

<template>
  <div class="full-background">
    <span class="title">Ready to upgrade your skin?</span>
    <CTAbutton />
  </div>
</template>

<style scoped>
div {
  position: relative;
  width: 100%;
  display: flex;
  min-height: 130px;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  padding: 30px;
}
.full-background {
  background-color: #ffc0cb;
}
.title {
  font-size: 3rem;
  font-weight: 700;
  color: white;
}
</style>

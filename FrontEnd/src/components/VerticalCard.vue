<!--Copy this boilerplate for easy component building-->
<script setup>
import { defineProps } from 'vue'

const Props = defineProps(['imgsrc', 'heading', 'text'])
</script>

<template>
  <div class="card-container">
    <img :src="imgsrc" />
    <div class="text-wrapper">
      <span class="title">{{ Props.heading }}</span>
      <span class="paragraph">{{ Props.text }}</span>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  width: 200px;
  min-height: 230px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  gap: 10px;

  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 20px;
  overflow: hidden;
}
.text-wrapper {
  width: 80%;
  height: max-content;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  color: white;
}
.title {
  font-size: 30px;
  font-weight: 700;
  text-align: center;
  color: black;
}
.paragraph {
  font-size: 15px;
  font-weight: 400;
  text-align: center;
  margin: 10px;
  color: hsla(0, 0%, 3%, 0.9);
}
img {
  border-radius: 15px;
  width: 200px;
  height: auto;
  border-radius: 10px;
}
</style>

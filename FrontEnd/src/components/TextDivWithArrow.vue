<!--Copy this boilerplate for easy component building-->
<script setup>
import { defineProps } from 'vue'
const Props = defineProps(['text', 'src', 'href'])
</script>

<template>
  <div class="container">
    <img :src="Props.src" alt="" />
    <a class="text-container" :href="Props.href" target="_blank">
      <h4 class="text">{{ Props.text }}</h4>

      <svg width="16px" height="16px" viewBox="0 0 16 16">
        <path d="M1 1 L16 8 L1 16 Z"></path>
      </svg>
    </a>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: black;
}
.container {
  width: 150px;
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  flex-direction: column;
  gap: 8px;
}
img {
  width: 150px;
  height: auto;
  border-radius: 10px;
}
.text-container {
  display: flex;
  width: 85%;
  height: 50%;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
</style>

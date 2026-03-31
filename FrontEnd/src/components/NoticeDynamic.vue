<!--Copy this boilerplate for easy component building-->
<script setup>
import { arrayProperties } from '@/Utils'
const Props = defineProps(['title', 'content', 'backgroundcolor', 'titlecolor', 'infocolor'])
</script>

<template>
  <div id="notice-container">
    <span class="notice-header-text">{{ Props.title }}</span>
    <span class="notice-info">{{ Props.content }}</span>
  </div>
</template>

<style scoped>
#notice-container {
  width: 100%;
  height: auto;
  padding: 10px 15px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 10px;
  background-color: v-bind(backgroundcolor);
  border-left: 5px solid var(--terracotta);
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
.notice-header-text {
  font-size: 1.2rem;
  font-family: 'Playfair Display', sans-serif;
  color: v-bind(titlecolor);
  font-weight: 500;
}
.notice-info {
  color: v-bind(infocolor);
  margin-left: 10px;
}
</style>

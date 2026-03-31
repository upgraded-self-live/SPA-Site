<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
import { onUpdate } from '@/Utils'
const terracotta = ref('#c9674a')
const props = defineProps(['text'])
//remove text if its a mobile screen.
const isMobile = ref(false)
onUpdate(() => {
  if (window.innerWidth <= 820) {
    isMobile.value = true
  } else {
    isMobile.value = false
  }
}, 500)
</script>

<template>
  <span class="line-text" v-if="!isMobile">
    <svg height="10" width="40" viewBox="0 0 40 10" :style="{ color: terracotta }">
      <line x1="0" y1="5" x2="40" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <span class="text">{{ text }}</span>
  </span>
</template>

<style scoped>
.line-text {
  color: var(--terracotta);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  width: max-content;
  gap: 10px;
  font-size: 0.7rem;
  letter-spacing: 0.5rem;
}
.text {
  font-family: 'DM Sans', sans-serif;
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
const Props = defineProps({
  text: { type: String },
  color: { type: String },
  linewidth: { type: String },
})
const viewbox = ref(`0 0 ${Props.linewidth} 10`)
</script>

<template>
  <div class="container">
    <svg height="10" :width="linewidth" :viewBox="viewbox" :style="{ color }">
      <line x1="0" y1="5" :x2="linewidth" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>

    <span class="text">{{ text }}</span>

    <svg height="10" :width="linewidth" :viewBox="viewbox" :style="{ color: color }">
      <line x1="0" y1="5" :x2="linewidth" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
  </div>
</template>

<style scoped>
.container {
  width: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}
.text{
    font-size: 1rem;
    color: v-bind(color);
}
</style>

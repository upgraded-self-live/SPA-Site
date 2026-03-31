<!--Copy this boilerplate for easy component building-->
<script setup>
import { onMounted } from 'vue'
import { ref } from 'vue'
//Accept color and background color using prop then set the element and backgrond accordingly
const props = defineProps(['background', 'color', 'text', 'circle'])
const color = ref('var(--terracotta)')
const background = ref('var(--terracotta-light)')
function AssignProps() {
  if (!props.background || props.color) {
    requestAnimationFrame(AssignProps)
  }
  color.value = props.color
  background.value = props.background
}
onMounted(() => {
  requestAnimationFrame(AssignProps)
})
</script>

<template>
  <div class="trivial-container">
    <span class="circle" v-if="props.circle == true"></span>
    <span class="content">{{ text }}</span>
  </div>
</template>

<style scoped>
.trivial-container {
  width: auto;
  height: 30px;
  border-radius: 20px;
  background-color: v-bind(background);
  color: v-bind(color);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 10px;
}
.circle {
  width: 10px;
  height: 10px;
  background-color: v-bind(background);
  border-radius: 50%;
}
.circle::before {
  content: '';
  width: 15px;
  height: 15px;
  border-radius: 50%;
  left: 0;
  top: 0;
  background-color: v-bind(color);
}
</style>

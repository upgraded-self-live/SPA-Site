<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
const props = defineProps(['direction', 'gap'])
const d = ref({})
const assign = (parent, obj) => {
  if (typeof obj === 'object') return Object.assign(parent, obj)
}
if (props.direction != 'column') {
  assign(d.value, { direction: 'row' })
} else {
  assign(d.value, { direction: props.direction })
}
assign(d.value, { gap: props.gap })
</script>

<template>
  <div class="comp-container">
    <slot></slot>
  </div>
</template>

<style scoped>
.comp-container {
  display: flex;
  flex-direction: v-bind(d.direction);
  gap: v-bind(d.gap);
  justify-content: space-evenly;
  align-items: center;
}
</style>

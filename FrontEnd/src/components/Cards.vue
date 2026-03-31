<!--Copy this boilerplate for easy component building-->
<script setup>
//Card container
import { ref } from 'vue'
const props = defineProps(['minWidth', 'minHeight'])
const constraints = ref({
  width: props.minWidth || '150px',
  height: props.minHeight || '150px',
})
</script>

<template>
  <div class="card-container">
    <slot />
  </div>
</template>

<style scoped>
.card-container {
  background-color: var(--warm-white);
  border-radius: 20px;
  padding: 20px;
  min-width: v-bind(constraints.width);
  min-height: v-bind(constraints.height);
  box-shadow: 10px 0 20px var(--mid-grey);
}
</style>

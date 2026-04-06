<!--Copy this boilerplate for easy component building-->
<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
const props = defineProps({
  position: { type: String, default: 'top-left' },
})
const router = useRouter()
const positioning = ref({
  topLeft: false,
  topRight: false,
  bottomLeft: false,
  bottomCenter: false,
  bottomRight: false,
})
switch (props.position) {
  case 'top-left':
    positioning.value.topLeft = true
    break
  case 'top-right':
    positioning.value.topRight = true
    break
  case 'bottom-left':
    positioning.value.bottomLeft = true
    break
  case 'bottom-center':
    positioning.value.bottomCenter = true
    break

  case 'bottom-right':
    positioning.bottomRight.value = true
    break
} //Reads the value of the prop.position then updates the reactive component boolean
function moveToPrevRoute() {
  router.back()
}
</script>

<template>
  <button
    @click="moveToPrevRoute"
    :class="{
      topLeft: positioning.topLeft,
      topRight: positioning.topRight,
      bottomleft: positioning.bottomLeft,
      bottomCenter: positioning.bottomCenter,
      bottomRight: positioning.bottomRight,
    }"
  >
    <!--Use the reactive component as a boolean value for the classes-->
    Back
  </button>
</template>

<style scoped>
button {
  background-color: transparent;
  border: none;
  color: var(--light-grey);
  font-family: 'DM Sans', sans-serif;
  font-size: 1.2rem;
  cursor: pointer;
  position: fixed;
  z-index: 101001010101;
}
button:hover {
  color: var(--terracotta);
}
.topLeft {
  left: 10px;
  top: 10px;
}
.topRight {
  right: 10px;
  top: 10px;
}
.bottomleft {
  left: 10px;
  bottom: 10px;
}
.bottomRight {
  right: 10px;
  bottom: 1px;
}
.bottomRight {
  left: 50%;
  bottom: 10px;
}
</style>

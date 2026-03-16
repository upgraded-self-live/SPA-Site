<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
const props = defineProps(['fontSize'])
const f = props.fontSize || ' 0.7rem'

const fs = ref(f)
const currentReactYear = ref('')
const currentYear = new Date().getFullYear()
if (currentYear) {
  currentReactYear.value = currentYear
}
</script>

<template>
  <p>&copy {{ currentReactYear }} UpgradedSelf.live</p>
</template>

<style scoped>
p {
  color: var(--light-grey);
  font-size: v-bind(fs);
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup>
const Props = defineProps(['error'])
</script>

<template>
  <div v-if="Props.error != '' || Props.error" class="Errror-container">
    <span class="error-text">{{ Props.error }}</span>
  </div>
</template>

<style scoped>
.Error-container {
  width: 200px;
  min-height: 50px;
  border-radius: 30px;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-backdrop-filter: blur(50px);
  backdrop-filter: blur(50px);
  color: white;
}
.error-text {
  color: white;
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup></script>

<template>
  <RouterLink to="/"><button class="CTA-button">Build your Routine</button></RouterLink>
</template>

<style scoped>
button {
  border-radius: v-bind(borderRadius);
  border: none;
  padding: 10px;
  cursor: pointer;
}
</style>

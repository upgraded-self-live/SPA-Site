<!--Copy this boilerplate for easy component building-->
<script setup></script>

<template>
  <RouterLink to="/quiz">
    <button class="call-to-action-button">BUILD YOUR ROUTINE</button>
  </RouterLink>
</template>

<style scoped>
button {
  font-family: 'DM Sans', sans-serif;
  min-width: 100px;
  padding: 10px 10px;
  text-align: center;
  cursor: pointer;
  border: none;
}
.call-to-action-button {
  background-color: var(--terracotta);
  color: var(--warm-white);
}
.call-to-action-button:hover {
  background-color: var(--terracotta-dark);
  transform: translateY(-5px);
}
</style>

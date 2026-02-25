<!--Copy this boilerplate for easy component building-->
<script setup>
import { defineProps } from 'vue'
const Props = defineProps(['text', 'src'])
</script>

<template>
  <div class="container">
    <img :src="Props.src" alt="" />
    <div class="text-container">
      <h2 class="text">{{ Props.text }}</h2>

      <svg width="16px" height="16px" viewBox="0 0 16 16">
        <path d="M1 1 L16 8 L1 16"></path>
      </svg>
    </div>
  </div>
</template>

<style scoped></style>

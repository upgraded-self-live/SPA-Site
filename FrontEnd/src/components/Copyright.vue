<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
const cd = ref(new Date().getFullYear())
</script>

<template>
  <div class="copyright">
    <p>Copyright © {{ cd }} UpgradedSelf.live. All rights reserved.</p>
  </div>
</template>

<style scoped>
p {
  color: white;
}
</style>

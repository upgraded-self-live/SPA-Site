<!--Copy this boilerplate for easy component building-->
<script setup>
const Props = defineProps(['title', 'content'])
</script>

<template>
  <div id="notice-container">
    <span class="notice-header-text">{{ Props.title }}</span>
    <span class="notice-info">{{ Props.content }}</span>
  </div>
</template>

<style scoped>
#notice-container {
  width: 100%;
  height: auto;
  padding: 10px 15px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 10px;
  background-color: var(--blush);
  border-left: 5px solid var(--terracotta);
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
.notice-header-text {
  font-size: 1.2rem;
  color: var(--terracotta);
  font-weight: 500;
}
.notice-info {
  color: var(--mid-grey);
  margin-left: 10px;
}
</style>

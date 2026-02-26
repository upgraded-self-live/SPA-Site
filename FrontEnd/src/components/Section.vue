<!--Copy this boilerplate for easy component building-->
<script setup>
const Props = defineProps(['title', 'subtitle', 'img'])
</script>

<template>
  <div v-if="!Props.img" class="no-image blur">
    <span class="title">{{ Props.title }}</span>
    <span class="subtitle">{{ Props.subtitle }}</span>
  </div>
  <div v-if="Props.img" class="image blur">
    <div class="text-container">
      <span class="title">{{ Props.title }}</span>
      <span class="subtitle">{{ Props.subtitle }}</span>
    </div>
    <img :src="Props.img || Props['img']" alt="" />
  </div>
</template>

<style scoped>
.blur {
  backdrop-filter: blur(50px);
  -webkit-backdrop-filter: blur(50px);
}
.no-image {
  position: relative;
  width: 100%;
  min-height: 150px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}
.image {
  width: 100%;
  min-height: 150px;
  padding: 16px;
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: center;
  justify-content: space-around;
}
.image > .text-container {
  width: 50%;
  display: flex;
  padding: 16px;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}
.image > img {
  width: 40%;
  height: 50%;
  image-rendering: auto;
  border-radius: 20%;
}
.title {
  font-size: 3rem;
}
.subtitle {
  font-size: 1.5rem;
  width: 80%;
  text-align: center;
}
</style>

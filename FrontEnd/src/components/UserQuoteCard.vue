<!--Copy this boilerplate for easy component building-->
<script setup>
import Trivial from './Trivial.vue'
import noProfileIcon from '@/components/Icons/default-no-picture.webp'
const props = defineProps([
  'name',
  'title',
  'workexperience',
  'quote',
  'imagesrc',
  'width',
  'height',
  'left',
  'top',
])
</script>

<template>
  <div class="card-container">
    <div class="pfp-title-container">
      <img :src="imagesrc" alt="" v-if="imagesrc" />
      <img
        :src="noProfileIcon"
        alt="profile picture"
        v-if="!imagesrc"
      /><!--If profile picture is not present, replace with default no profile picture place holder-->
      <!--Profile picture-->
      <!--title in company-->
      <Trivial circle="false" :text="title" color="#a8503a" background="#e8896e" />
    </div>
    <div class="header-text-container">
      <!--Name--><span class="Name-content">{{ name }}</span>
      <span class="work-experience-content">{{ workexperience }}</span>
    </div>
    <div class="Quote-container">
      <!--Quote--><span class="quote-content">"{{ quote }}"</span>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  position: absolute;
  left: v-bind(left);
  top: v-bind(top);
  border-radius: 10px;
  width: v-bind(width);
  height: v-bind(height);
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
  flex-shrink: 2;
  background-color: var(--cream);
  padding: 30px;
}
.pfp-title-container {
  width: 100%;
  height: 25%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
}
.pfp-title-container > img {
  image-rendering: auto;
  border-radius: 50%;
  border: 3px solid var(--terracotta);
  width: 30%;
  height: auto;
}
.Name-content {
  font-family: 'Playfair Display', sans-serif;
  font-size: 1.5rem;
}
.header-text-container {
  width: 100%;
  height: 30%;
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: flex-start;
}
.work-experience-content {
  width: block;
  font-size: 1rem;
  color: var(--terracotta);
}
.Quote-container {
  width: 100%;
  height: 25%;
  display: flex;
  align-items: flex-start;
}
.quote-content {
  font-style: italic;
  color: var(--mid-grey);
}
</style>

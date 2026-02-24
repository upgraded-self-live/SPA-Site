<!--Copy this boilerplate for easy component building-->
<script setup>
import { defineProps, onMounted } from 'vue'
import Img500 from './Img500.vue'
const Props = defineProps(['heading', 'subheading', 'imagesrc'])
console.log(Props.imagesrc)
</script>

<template>
  <div class="container">
    <div class="Text-wrapper">
      <span class="title">{{ Props.heading }}</span>
      <span class="sub-title">{{ Props.subheading }}</span>
    </div>
    <Img500 :propsrc="Props.imagesrc" class="header-img"/>
    
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  min-height: 600px;
  position: relative;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

 
  backdrop-filter: blur(50px);
  -webkit-backdrop-filter: blur(50px) ;

  padding: 30px ;
}
.Text-wrapper {
  min-width: 500px;
  height: max-content;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;

  color: black;
}
.title {
  font-size: 60px;
  font-weight: 700;
}
.sub-title {
  font-size: 30px;
  font-weight: 400;
  color: hsla(0, 0%, 3%, 0.9);
  margin-left: 10px;
}
.header-img{
    border-radius: 50%;
}
</style>

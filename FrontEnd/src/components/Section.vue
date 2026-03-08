<!--Copy this boilerplate for easy component building-->
<script setup>
import { onMounted, ref } from 'vue'
const Props = defineProps(['title', 'subtitle', 'img'])
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
gsap.registerPlugin(ScrollTrigger)

function setScrollTrigger(selection, triggerel, object) {
  try {
    if (typeof object != 'object') {
      return 'Object expected @ argument 2'
    }
    return gsap.from(selection, {
      ...object,
      scrollTrigger: { trigger: triggerel, start: 'top 80%', end: 'bottom 20%' , scrub: true},
    })
  } catch (e) {
    console.error(e)
    return gsap.from(selection, { ...object });
  }
}
const title = ref(null)
const sub_title = ref(null)
onMounted(() => {
  setScrollTrigger(title.value, title.value, { opacity: 0, y: 50, duration: 1, ease: 'power2.out' })
  setScrollTrigger(sub_title.value, title.value, { opacity: 0, y: 50, duration: 1, ease: 'power2.out' })
})
</script>

<template>
  <div v-if="!Props.img" class="no-image blur">
    <span ref="title" class="s-title">{{ Props.title }}</span>
    <span ref="sub_title" class="s-subtitle">{{ Props.subtitle }}</span>
  </div>
  <div v-if="Props.img" class="image blur">
    <div class="text-container">
      <span ref="title" class="s-title">{{ Props.title }}</span>
      <span ref="sub_title" class="s-subtitle">{{ Props.subtitle }}</span>
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
.s-title {
  font-size: 3rem;
}
.s-subtitle {
  font-size: 1.5rem;
  width: 80%;
  text-align: center;
}
</style>

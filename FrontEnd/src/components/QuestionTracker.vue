<!--Copy this boilerplate for easy component building-->
<script setup>
import { cookieUtils, onUpdate } from '@/Utils'
import { ref } from 'vue'

const doneColor = ref('#8a9e8c')
const questionNumber = ref(1)
const cookie = new cookieUtils()
const getUgrdSession = () => {
  return cookie?.getFromCookie('ugrd_session')
}
const getQuizNumber = () => {
  const obj = getUgrdSession()
  return obj != undefined ? obj.quizProgress : 1
}
onUpdate(() => {
  if (questionNumber.value) {
    questionNumber.value = getQuizNumber() || 1
  }
}, 100)
</script>

<template>
  <div class="container" v-if="questionNumber == 1">
    <div class="circle-container active">
      <span class="c-white">1</span>
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--Second marker-->
  <div class="container" v-if="questionNumber == 2">
    <div class="circle-container done">
      <span class="c-white"
        >1
        <!--Replace with checkmark if possible--></span
      >
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container active">
      <span class="c-white">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--Third marker-->
  <div class="container" v-if="questionNumber == 3">
    <div class="circle-container done">
      <span class="c-white">1</span>
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-white">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container active">
      <span class="c-white">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--Fourth marker-->
  <div class="container" v-if="questionNumber == 4">
    <div class="circle-container">
      <span class="c-white">1</span>
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-white">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-white">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container active">
      <span class="c-white">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--Fifth marker-->
  <div class="container" v-if="questionNumber == 5">
    <div class="circle-container done">
      <span class="c-white">1</span>
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-white">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-white">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: doneColor }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container done">
      <span class="c-whitey">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container active">
      <span class="c-whitey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--Sixth marker-->
  <div class="container" v-if="questionNumber == 6">
    <div class="circle-container active">
      <span class="c-white">1</span>
    </div>
    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">2</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">3</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">4</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">5</span>
    </div>

    <svg height="10" :width="30" viewBox="0 0 30 10" :style="{ color: 'var(--light-grey)' }">
      <line x1="0" y1="5" :x2="30" y2="5" stroke="currentColor" stroke-width="1" />
    </svg>
    <div class="circle-container">
      <span class="c-light-grey">6</span>
    </div>
  </div>
  <!--End of Markers-->
</template>

<style scoped>
.c-light-grey {
  color: var(--light-grey);
}
.c-white {
  color: var(--white);
}
.container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.circle-container {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 1px solid var(--light-grey);
}
.active {
  background-color: var(--terracotta);
}
.done {
  background-color: v-bind(doneColor) !important;
}
</style>

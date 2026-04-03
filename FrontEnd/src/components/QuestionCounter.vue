<!--Copy this boilerplate for easy component building-->
<script setup>
import { cookieUtils, onUpdate } from '@/Utils'
import { ref } from 'vue'
const totalNumofQuestions = ref(6)
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
  questionNumber.value = getQuizNumber()
}, 100)
</script>

<template>
  <div id="counterContaioner" v-if="questionNumber !== totalNumofQuestions">
    <span class="info-text"
      ><span class="c-terracotta">{{ questionNumber }}</span> of
      <span class="n">{{ totalNumofQuestions }}</span> questions</span
    >
  </div>
  <div id="counterContaioner" v-if="questionNumber === totalNumofQuestions">
    <span class="info-text"
      ><span class="c-terracotta">{{ questionNumber }}</span> of
      <span class="c-terracotta">{{ totalNumofQuestions }}</span> questions</span
    >
  </div>
</template>

<style scoped>
#counterContaioner {
  display: block;
  height: 20px;
  width: auto;
  text-align: center;
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.3rem;
  margin-left: 10px;
}
.n {
  color: var(--charcoal);
}
</style>

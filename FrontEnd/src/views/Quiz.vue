<!--Copy this boilerplate for easy component building-->
<script setup>
/*
            --Level Configuration--         
This script will manage the quiz questions utilizing vue dynamic rendering and conditional program control
Steps:
1.I will make a global reactive element called question number
2.Use v-if to check question number and map to its div element for .e.x. <div v-if="questionNum ==2 ">**Questions to render**<!div>
3. I will create a multi selection element:
3.1. When the user clicks on one of the choices the "chosen" class is toggled to it 
3.2. When the user clicks next question, the elements with the "chosen" class have their attributes scanned and stored in a cookie called "ugrd_session"
4. I will add a question tracker component allowing user to know what question number they are on using the ugrd_session cookie.
Question number will be stored in the ugrd_session cookie
This documentation is subject to change.*/
import { ref } from 'vue'
import { cookieUtils, s, p } from '@/Utils'
import STextLine from '@/components/STextLine.vue'
import QuestionTracker from '@/components/QuestionTracker.vue'
import QuestionCounter from '@/components/QuestionCounter.vue'
const questionNum = ref(1)
const cookies = new cookieUtils()
let ugrdSessionOG = cookies.getFromCookie('ugrd_session')
const footerEl = ref()
const ChoicesContainer = ref()
//Update the global session cookie variable, Repetition solution
function updateGlobalugrdSessionCookie() {
  ugrdSessionOG = cookies.getFromCookie('ugrd_session')
}
//1 Hour for setting cookie
const hour = 60 * 60
//Check if the global ugrd_session cookie exist, if not create it.
if (!ugrdSessionOG) {
  const ugrd_session = {
    quizProgress: 1,
    data: {},
  }
  const savableVersion = s(ugrd_session)
  console.log(savableVersion)
  cookies.setItemInCookie('ugrd_session', savableVersion, hour)
  updateGlobalugrdSessionCookie()
}
if (ugrdSessionOG && ugrdSessionOG['quizProgress'] > 1) {
  questionNum.value = ugrdSessionOG['quizProgress']
}
function prevQuestion() {
  if (questionNum.value > 1) {
    questionNum.value = questionNum.value - 1
    const quizsetter = Object.assign(ugrdSessionOG, { quizProgress: questionNum.value })
    console.log(quizsetter)
    cookies.setItemInCookie('ugrd_session', s(quizsetter), hour)
    updateGlobalugrdSessionCookie()
  }
}
function nextQuestion() {
  if (questionNum.value < 6) {
    questionNum.value = questionNum.value + 1
    //function to grab values of elements and return an object
    const quizsetter = Object.assign(ugrdSessionOG, { quizProgress: questionNum.value })
    console.log(quizsetter)
    cookies.setItemInCookie('ugrd_session', s(quizsetter), hour) //Must stringify before saving
    updateGlobalugrdSessionCookie()
  }
}
</script>

<template>
  <header>
    <span class="brand">UGRD.LIVE</span>
    <QuestionTracker />
    <RouterLink to="/">SAVE & EXIT</RouterLink>
  </header>

  <div id="Main-container" data-question-mapper="1" v-if="questionNum === 1">
    <div id="Main-content">
      <STextLine text="STEP 1 SKIN TYPE" />
      <div id="question-container">
        <span class="h3"
          >How does your skin feel by <span class="italic c-terracotta">midday</span></span
        >
        <span class="info-text">Think about an average day, not after exercise or stress.</span>
      </div>
      <div :ref="ChoicesContainer" id="ChoicesContainer"></div>
      <div class="button-container">
        <button @click="nextQuestion">Next Step ⏭️</button>
      </div>
    </div>
  </div>

  <div id="Main-container" data-question-mapper="2" v-if="questionNum === 2">
    <div id="Main-content">
      <h1>Main-Concerns</h1>
      <div class="max-width-flex-row-space-between">
        <span>{{ questionNum }} of 6 questions</span>
        <div class="button-container">
          <button @click="prevQuestion">back</button>
          <button @click="nextQuestion">Next</button>
        </div>
      </div>
    </div>
  </div>
  <footer :ref="footerEl"><!--Style this for quiz progress--></footer>
  <QuestionCounter />
</template>

<style scoped>
.brand {
  font-size: 2rem;
  font-family: 'Playfair Display', sans-serif;
  font-weight: 1rem;
}
header {
  position: fixed;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  z-index: 99999;
  min-height: 100px;
  width: 100%;
  border-bottom: 1px solid var(--light-grey);
  padding: 30px;
}
a {
  color: var(--light-grey);
  text-decoration: none;
}
a:hover {
  color: var(--mid-grey);
}
#Main-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#Main-content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
  padding: 30px;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.1rem;
  margin-left: 10px;
}
#question-container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.button-container {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
button {
  min-width: 150px;
  height: 40px;
  border-radius: 5px;
  cursor: pointer;
}
</style>

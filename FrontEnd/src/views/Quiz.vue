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
import { onUpdate, cookieUtils } from '@/Utils'
import QuestionTracker from '@/components/QuestionTracker.vue'
import QuestionCounter from '@/components/QuestionCounter.vue'
/*---Imports of questions---*/
import Question1 from '@/components/Question1.vue'
import Question2 from '@/components/Question2.vue'
import Question3 from '@/components/Question3.vue'
import Question4 from '@/components/Question4.vue'
import Question5 from '@/components/Question5.vue'
import Question6 from '@/components/Question6.vue'
const questionNum = ref(1)
const footerEl = ref()
const cookies = new cookieUtils()
const getCurrentQuestionNum = () => {
  const ugrd_session = cookies.getFromCookie('ugrd_session')
  if (!ugrd_session) {
    return 1
  }
  return ugrd_session.quizProgress
}
onUpdate(() => {
  questionNum.value = getCurrentQuestionNum()
}, 100)
</script>

<template>
  <header>
    <span class="brand">UGRD.LIVE</span>
    <QuestionTracker />
    <RouterLink to="/">SAVE & EXIT</RouterLink>
  </header>

  <div class="Main-container" data-question-mapper="1" v-if="questionNum === 1" id="Skin-type">
    <Question1 />
  </div>

  <div class="Main-container" data-question-mapper="2" v-if="questionNum === 2">
    <Question2 />
  </div>
  <div class="Main-container" data-question-mapper="3" v-if="questionNum === 3">
    <Question3 />
  </div>
  <div class="Main-container" data-question-mapper="4" v-if="questionNum === 4">
    <Question4 />
  </div>
  <div class="Main-container" data-question-mapper="5" v-if="questionNum === 5">
    <Question5 />
  </div>
  <div class="Main-container" data-question-mapper="6" v-if="questionNum === 6">
    <Question6 />
  </div>
  <footer ref="footerEl"><!--Style this for quiz progress--></footer>
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
  background: transparent;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
a {
  color: var(--light-grey);
  text-decoration: none;
}
a:hover {
  color: var(--mid-grey);
}
.Main-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-shrink: 2;
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
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  gap: 10px;
}
</style>

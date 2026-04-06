<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { cookieUtils, s, p, onUpdate, toggleActive, accessSessionStorage } from '@/Utils'
import STextLine from '@/components/STextLine.vue'
const cookies = new cookieUtils()
let ugrdSessionGlobal = cookies.getFromCookie('ugrd_session')
const questionNum = ugrdSessionGlobal?.quizProgress || 1
const footerEl = ref()
const ChoicesContainer = ref()
const errorElVal = ref()
const router = useRouter()
onMounted(() => {
  getUserChoicesFromSessionStorage()
})
//Update the global session cookie variable, Repetition solution
function updateGlobalugrdSessionCookie() {
  ugrdSessionGlobal = cookies.getFromCookie('ugrd_session')
}
if (!ugrdSessionGlobal) {
  const ugrd_session = {
    quizProgress: 1,
    data: {},
  }
  const savableVersion = s(ugrd_session) //stringified version
  console.log(savableVersion)
  cookies.setItemInCookie('ugrd_session', savableVersion, hour)
  updateGlobalugrdSessionCookie()
}
const hour = 60 * 60
function fetchActiveChoicesFromQuestions() {
  try {
    const chosenElArray = ChoicesContainer.value.querySelectorAll('.active') //Gets all active element from the reactive global container
    if (!chosenElArray || chosenElArray.length === 0) {
      errorElVal.value = 'Select atleast one option'
      throw new error('User must select an option to proceed')
      return
    }
    const questionType = ChoicesContainer.value.id //Gets the id of the container for identification of question type
    const answersArray = [] //Stores answers
    if (chosenElArray.length === 1) {
      return { [questionType]: chosenElArray[0]?.getAttribute('data-value') } //Returns if there is only one selected element
    }
    chosenElArray.array.forEach((element) => {
      answersArray.push(element.getAttribute('data-value')) //adds the data-value attribute of the element to the array
    })
    console.log({ [questionType]: answersArray })
    return { [questionType]: answersArray } //returns an array mapped with its question type for easy identification in backend and uniqueness
  } catch (e) {
    console.error(e)
    return null
  }
}
function SaveUserChoiceInSessionStorage() {
  const chosenElArray = ChoicesContainer.value.querySelectorAll('.active')
  const sessionStorage = new accessSessionStorage()
  const valArray = []
  chosenElArray.forEach((e) => {
    valArray.push(e.textContent)
  })
  sessionStorage.set(questionNum, valArray)
}
function getUserChoicesFromSessionStorage() {
  try {
    const sessionStorage = new accessSessionStorage()
    const chosenElArray = ChoicesContainer.value.querySelectorAll('.choice')

    const g = sessionStorage.get(questionNum)
    if (!g) {
      return
    }
    chosenElArray.forEach((e) => {
      //Loops through the fetched array from session
      if (e.textContent === g) {
        e.classList.add('active') //Adds active if the text-content matches
      }
    })
  } catch (e) {
    console.error(e)
  }
}
const getCurrentQuestionNum = () => {
  const ugrd_session = cookies.getFromCookie('ugrd_session')
  if (!ugrd_session) {
    return 1
  }
  return ugrd_session.quizProgress
}
function prevQuestion() {
  try {
    const questionNum = getCurrentQuestionNum()
    const newIdx = questionNum - 1
    ugrdSessionGlobal = Object.assign(ugrdSessionGlobal, { quizProgress: newIdx }) //Save the new index to the cookie
    //Stringify before saving saving it to the cookie
    console.log(ugrdSessionGlobal)
    cookies.setItemInCookie('ugrd_session', s(ugrdSessionGlobal), hour)
    console.log('Index changed')
  } catch (e) {
    console.error(e)
  }
}
function nextQuestion(none = false) {
  try {
    SaveUserChoiceInSessionStorage()
    const questionAnswers = fetchActiveChoicesFromQuestions() //Fetch all question answers
    if (!questionAnswers) {
      return
    }
    let newIdx = none ? questionNum : questionNum + 1
    ugrdSessionGlobal = Object.assign(ugrdSessionGlobal, { quizProgress: newIdx })
    const scopedSession = {
      ...ugrdSessionGlobal,
      data: { ...ugrdSessionGlobal.data, ...questionAnswers },
    }
    ugrdSessionGlobal = scopedSession
    console.log(ugrdSessionGlobal)
    cookies.setItemInCookie('ugrd_session', s(ugrdSessionGlobal), hour)
    if (none) {
      router.push('/routine-builder')
    }
  } catch (e) {
    console.warn(e)
  }
}
</script>

<template>
  <div class="Main-content">
    <STextLine text="STEP 4 - SKINCARE EXPERIENCE" />
    <div id="question-container">
      <span class="h3"
        >How familiar are you with <span class="italic c-terracotta">skincare?</span></span
      >
      <span class="info-text">This shapes how technical our product recommendations get.</span>
    </div>
    <div ref="ChoicesContainer" id="exp" class="card-container-flex" data-allowed="single">
      <!--Container starts-->
      <div class="choice" @click="toggleActive($event, ChoicesContainer)" data-value="beginner">
        <!--This system is measured from 1 to 4 with one being the best and 4 being the worse-->
        <span class="h2 emoji">🌱</span>
        <div class="text-container-flex-column">
          <span class="main-text">Beginner</span>
          <span class="info-text">Start from scratch</span>
        </div>
      </div>

      <div
        class="choice"
        @click="toggleActive($event, ChoicesContainer)"
        data-value="some knowledge"
      >
        <span class="h2 emoji">📖</span>
        <div class="text-container-flex-column">
          <span class="main-text">Some knowledge</span>
          <span class="info-text">You know the basics</span>
        </div>
      </div>

      <div class="choice" @click="toggleActive($event, ChoicesContainer)" data-value="intermediate">
        <span class="h2 emoji">🔬</span>
        <div class="text-container-flex-column">
          <span class="main-text">Intermediate</span>
          <span class="info-text">Knows actives</span>
        </div>
      </div>

      <div class="choice" @click="toggleActive($event, ChoicesContainer)" data-value="advanced">
        <span class="h2 emoji">🎓</span>
        <div class="text-container-flex-column">
          <span class="main-text">Advanced</span>
          <span class="info-text">Read ingredient list</span>
        </div>
      </div>
      <!--Container ends -->
    </div>
    <div class="button-container">
      <button @click="prevQuestion" id="prevButton">Back</button>
      <button @click="nextQuestion(true)" id="nextButton">Build my routine</button>
    </div>
  </div>
  <div class="error-container" v-if="errorElVal">
    <span class="error-text">{{ errorElVal }}</span>
  </div>
</template>

<style scoped>
.error-container {
  background-color: var(--terracotta-transparent);
  min-width: 150px;
  min-height: 60px;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  animation: slide-in 500ms ease-out;
  top: 90%;
  right: 0;
  padding: 10px;
  color: var(--terracotta-dark);
}
@keyframes slide-in {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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
  gap: 10px;
}
button {
  min-width: 150px;
  min-height: 40px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  gap: 10px;
  font-size: 1rem;
  font-family: 'DM Sans', sans-serif;
  padding: 5px;
}
.Main-content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
  flex-shrink: 1;
  padding: 30px;
}
#nextButton {
  background-color: var(--charcoal);
  border: none;
  color: var(--white);
}
#prevButton {
  border: 1px solid var(--light-grey);
  color: var(--charcoal);
}
#nextButton:hover {
  background-color: var(--terracotta);
  transform: translateY(-10px);
}
.choice {
  min-width: 250px;
  padding: 30px;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  border-radius: 10px;
  border: none;
  background-color: var(--white);
  cursor: pointer;
}
.choice:hover {
  border: 1px solid var(--light-grey);
  transform: translateY(-10px);
  box-shadow: 0 5px 20px 0 var(--light-grey);
}
.choice:hover > .emoji {
  transform: scale(1.19) translateY(-5px) !important;
}
.choice:active {
  transform: scale(0.9999999);
  background-color: var(--terracotta-light);
}
.active {
  border: 1px solid var(--terracotta);
  background-color: var(--terracotta-transparent);
}
.text-container-flex-column {
  width: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: center;
}
.text-container-flex-column .info-text {
  display: block;
  white-space: nowrap;
  font-size: 0.9rem;
}
.text-container-flex-column .main-text {
  font-size: 1.2rem;
  color: var(--charcoal);
}
.card-container-flex {
  width: 100%;
  min-height: 300px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}
a {
  text-decoration: none;
}
</style>

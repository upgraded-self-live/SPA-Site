<!--Copy this boilerplate for easy component building-->
<script setup>
//Get current route data
//update the title of the page if the request is completed
/*
--Component Plan--
-Make 2 different components, one to handle fetch and create the result cookie
--The other component will get the cookie and display results
*/
import { ref, onMounted } from 'vue'
import { cookieUtils, s } from '@/Utils'
import DynamicDesignedQuoteCard from '@/components/DynamicDesignedQuoteCard.vue'
import PrevRoute from '@/components/PrevRoute.vue'
const completed = ref(false) //Stores the state of the routine builder
const quotes = [
  {
    author: 'Amit Kalantri',
    quote: 'Take care of your skin and your confidence will take care of itself.',
  },
  { author: 'Amit Kalantri', quote: 'Skincare is like a workout for your skin.' },
  { author: 'unknown', quote: 'A beautiful skin is no miracle, but rather a commitment.' },
  {
    author: 'Jess C. Scott',
    quote:
      'Be patient. Your skin took a while to deteriorate. Give it some time to reflect a calmer inner state.',
  },
  { author: 'Huda Kattan', quote: 'Your skin is an investment, not an expense.' },
]
const chosenQuote = ref({})
const cookies = new cookieUtils()
const getUgrdSessionCookie = () => {
  console.log(cookies.getFromCookie('ugrd_session')['data'])
  return s(cookies.getFromCookie('ugrd_session')['data'])
}
function loadRandomQuote() {
  chosenQuote.value = quotes[Math.floor(Math.random() * 4)]
}
async function buildRoutine() {
  const request = await fetch('http://127.0.0.1:8000/build', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: getUgrdSessionCookie(),
  })
  if (request.ok) {
    const response = await request.json()
    console.log(response)
    completed.value = true
  }
}
onMounted(async () => {
  loadRandomQuote()
  await buildRoutine()
})
</script>

<template>
    <PrevRoute/>
  <div
    class="content-wrapper full-height h-q-width flex flex-center flex-column g-30 p-fix-center"
    v-if="!completed"
  >
    <header class="g-30">
      <span class="h1 emoji">🌿</span>
      <h1>We are building your <span class="c-terracotta italic">Routine</span></h1>
    </header>
    <span class="info-text text-center"
      >We are building the best routine possible based on your answers.</span
    >
    <DynamicDesignedQuoteCard
      :quote="chosenQuote.quote"
      :author="chosenQuote.author"
      :designonecontent="`'${chosenQuote.author}''`"
      :designtwocontent="`'${chosenQuote.quote}''`"
    />
  </div>
</template>

<style scoped>
.text-center {
  text-align: center;
}
.content-wrapper {
  width: 100vw;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.full-height {
  height: 100vh !important;
}
.flex {
  display: flex;
}
.flex-column {
  flex-direction: column;
}
.flex-row {
  flex-direction: row;
}
.flex-center {
  align-items: center;
  justify-content: center;
}
.g-30 {
  gap: 30px;
}
header {
  display: flex;
  text-align: center;
  flex-direction: column;
  align-items: center;
}
.p-fix-center {
  position: fixed;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
}
.h-q-width {
  width: 80vw;
}
.emoji {
  animation: hover 3s 10ms infinite ease-in-out;
}
@keyframes hover {
  0% {
    transform: translateY(5px) rotateZ(0);
  }
  50% {
    transform: translateY(-10px) rotateZ(10deg);
  }
  100% {
    transform: translateY(5px) rotateZ(0);
  }
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.6rem;
  margin-left: 10px;
}
.mini-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--light-grey);
  font-size: 0.6rem;
}
</style>

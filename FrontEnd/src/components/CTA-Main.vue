<!--Copy this boilerplate for easy component building-->
<script setup>
import { cookieUtils } from '@/Utils'
const c = new cookieUtils()

function updateCurrentChoiceAndStyles(event /* this grabs the element that invoked the event */) {
  //This function will update the styles and classes of each element in the #choices element
  const elArray = document.querySelectorAll('.choice')
  elArray.forEach((e) => {
    e.classList.remove('active-choice') //removes the active button
    if (!event.target.classList.contains('active-choice') && event.target.tagName === 'BUTTON') {
      event.target.classList.add('active-choice')
    }
    grabCurrentChoice(event.target)
  })
}
function grabCurrentChoice(el) {
  /* this function will grab the argument element and fetch the class */
  if (!el) {
    throw new error('Argument is not provided')
  }
  try {
    if (el.classList.contains('active-choice')) {
      const attrValue = el.getAttribute('data-choice')
      const s = c.setItemInCookie('skin-type', attrValue, 60);
      const ugrd_session = {
        quizProgress: '1',
        data: {
          skinType: attrValue
        }
      }
      const savable_version = JSON.stringify(ugrd_session)
      c.setItemInCookie('ugrd_session', savable_version, 60) // this cookie will be used to track the quiz progress and make sure that the user is on the right question when they go back to the quiz after leaving it for a while
    }
  } catch (e) {
    throw new error(e)
  }
}
</script>

<template>
  <!--This is the main call to action -->
  <div id="main-container">
    <div id="header">
      <span id="def-text">STEP 1 - SKIN TYPE QUIZ</span>
      <ul>
        <li class="page-marker" data-active="true"></li>
        <li class="page-marker"></li>
        <li class="page-marker"></li>
      </ul>
    </div>
    <div id="content">
      <!--Container the main questions and CTA button-->
      <h2 class="question">What best describes your skin by midday?</h2>
      <div class="grid2x2" id="choices">
        <button class="choice" @click="updateCurrentChoiceAndStyles" data-choice="Dry">
          <span class="main-button-info">Dry</span
          ><span class="secondary-button-info">Tight/Flaky</span>
        </button>
        <button class="choice" @click="updateCurrentChoiceAndStyles" data-choice="Oily">
          <span class="main-button-info">Oily</span>
          <span class="secondary-button-info">Shiny/Slick</span>
        </button>
        <button class="choice" @click="updateCurrentChoiceAndStyles" data-choice="Combination">
          <span class="main-button-info">Combined</span
          ><span class="secondary-button-info">T-Zone/U-Zone</span>
        </button>
        <button class="choice" @click="updateCurrentChoiceAndStyles" data-choice="Normal">
          <span class="main-button-info">Normal</span
          ><span class="secondary-button-info">Balanced & Calm</span>
        </button>
      </div>
      <RouterLink to="/" class="CTA-button-container"
        ><button class="call-to-action-button" style="border-radius: 10px">
          Next Question: Your Budget ➡
        </button></RouterLink
      >
    </div>
    <div class="footer">
      <span class="secondary-button-info">⭐No Accounts Needed -- Takes 60 Seconds</span>
    </div>
  </div>
  <!--This component will be style by a parent component like Home.vue-->
</template>

<style scoped>
.CTA-button-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}
.call-to-action-button {
  font-family: 'DM Sans', sans-serif;
  width: 60%;
  height: 60px;
  padding: 10px 10px;
  text-align: center;
  cursor: pointer;
  border: none;
  background-color: var(--terracotta);
  color: var(--warm-white);
}
.call-to-action-button:hover {
  background-color: var(--terracotta-dark);
  transform: translateY(-5px);
}
.question {
  font-size: 2rem;
}
#def-text {
  color: var(--terracotta);
  font-family: 'DM Sans', sans-serif;
}
ul {
  width: max-content;
  min-height: 30px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  gap: 10px;
}
#header {
  min-height: 10%;
  width: 100%;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
li {
  list-style: none;
}
.page-marker {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: var(--light-grey);
}
.page-marker[data-active='true'] {
  width: 30px;
  height: 10px;
  border-radius: 10px;
  background-color: var(--terracotta);
}
#content {
  height: 80%; /* footer will be 15% in height*/
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 1;
  gap: 20px;
  padding: 0 10px;
} /*Increased gap to fit button properly*/
.footer {
  height: 5%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.grid2x2 {
  width: 100%;
  min-height: 50%;
  display: grid;
  grid-template-rows: repeat(2, 1fr);
  grid-template-columns: repeat(2, 50%);
  gap: 20px; /* Adds 15px space between grid cells */
  justify-items: center; /* Centers items horizontally */
  align-items: center; /* Centers items vertically */
} /*Correct pixel size of each cell because its too big */
.main-button-info {
  font-size: 1.2rem;
  color: var(charcoal);
}
.secondary-button-info {
  font-size: 0.6rem;
  color: var(--light-grey);
}
.choice {
  background-color: transparent;
  border-radius: 10px;
  height: 100px;
  width: 90%;
  border: 1px solid var(--mid-grey);
  padding: 10px 20px;
  color: var(--mid-grey);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
}
.choice:hover {
  border: 1px solid var(--terracotta);
  color: var(--terracotta) !important;
}
.active-choice {
  background-color: var(--terracotta) !important;
  color: var(--warm-white) !important;
}
.active-choice:hover {
  background-color: var(--terracotta) !important;
  color: var(--warm-white) !important;
  border: 1px solid var(--terracotta);
}
</style>

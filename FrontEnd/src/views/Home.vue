<!--Copy this boilerplate for easy component building-->
<script setup>
import { gsap } from 'gsap'
import { ref, onMounted } from 'vue'
import Cards from '@/components/Cards.vue'
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import CTAMain from '@/components/CTA-Main.vue'
import Proof from '@/components/Proof.vue'
const num_of_questions = ref(3) // This reactive component is used for the description in the header under the header text with class ".info-text".
onMounted(() => {
  const selected_elements = document.querySelectorAll('.show-up') //Loop through each element with the show-up class
  selected_elements.forEach((i) => {
    gsap.from(i, { opacity: 0, y: 20, duration: 0.7, delay: 0, ease: 'power2.out' })
    //add the gsap.from animation for the intro animation
  })
})
</script>

<template>
  <Navigation />
  <header>
    <section class="left-section">
      <STextLine text="PERSONALIZED ROUTINE" class="show-up" />
      <div class="Main-text-container">
        <span class="header-text-container">
          <h1 class="show-up">Your Skin,</h1>
          <h1 class="force-sameline ws-07 show-up">
            Your
            <span class="color-terracotta h1 show-up">Ritual.</span
            ><!--I made sure that the ritual stands out using color-terracotta -->
          </h1>
        </span>
        <span class="info-text show-up">
          Answer {{ num_of_questions }} questions and we will build you a personalized skincare
          routine caterred to your skin type, budget and life-style. - no guesswork
        </span>
      </div>
      <CTAMain id="Main-CTA" />
    </section>
    <section class="right-section">
      <!--This will have gradient background with absolute positioned cards-->
      <div class="gradient-terracottaX2-light">
        <Cards class="card morning-card show-up" maxWidth="300px" maxHeight="300px"
          ><!--Morning Routine Card-->
          <span class="time-meridiem">AM</span>
          <div class="card-text-container">
            <span class="fs-2rem">🌅</span>
            <h2 class="card-header">Morning Routine</h2>
            <p class="card-description">Cleanser, Toner, Moisturizer, Sunscreen</p>
          </div>
        </Cards>

        <Cards class="card night-card show-up" maxWidth="300px" maxHeight="300px"
          ><!--Evening Routine Card-->
          <span class="time-meridiem">PM</span>
          <div class="card-text-container">
            <span class="fs-2rem">🌜</span>
            <h2 class="card-header">Evening Routine</h2>
            <p class="card-description">2x Cleanser, Toner, Moisturizer</p>
          </div>
        </Cards>
      </div>
    </section>
  </header>
  <main>
    <Proof />
  </main>
  <footer></footer>
</template>

<style scoped>
header {
  height: 120vh;
  width: 100%;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 140px 0 0 0;
  overflow: hidden;
}
main {
  width: 100%;
  height: auto;
}
footer {
  width: 100%;
  min-height: 100px;
}
.left-section {
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 20px;
  padding: 10px 30px;
}
.right-section {
  width: 60%;
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding: 10px;
}
.card .time-meridiem {
  padding: 5px;
  background-color: var(--terracotta);
  text-align: center;
  color: var(--warm-white);
  border-radius: 50%;
}
.right-section .morning-card {
  position: absolute;
  top: 10%;
  left: 20%;
  transform: rotate(15deg);
}
.right-section .night-card {
  position: absolute;
  top: 60%;
  left: 40%;
  transform: rotate(-15deg);
}
.card-description {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  color: var(--mid-grey);
}
.right-section .card {
  width: auto;
  height: 20%;
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
}
.Main-text-container {
  width: 100%;
  height: 40%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.header-text-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}
.color-terracotta {
  color: var(--terracotta-dark);
}
.force-sameline {
  width: max-content;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
}
.h1 {
  font-size: 4rem; /* Made this h1 for the inline span*/
}
.ws-07 {
  word-spacing: 0.7rem;
  gap: 0.7rem;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.1rem;
}
.show-up {
  opacity: 1;
}
.gradient-terracottaX2-light {
  background: radial-gradient(var(--terracotta), var(--terracotta-light));
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
}
.fs-2rem {
  font-size: 2rem;
}
#Main-CTA {
  min-height: 60%;
  width: 100%;
  border-radius: 5px;
  padding: 20px;
  background-color: var(--warm-white);
  box-shadow: 0px 5px 5px var(--mid-grey);
  gap: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>

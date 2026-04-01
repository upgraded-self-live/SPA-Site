<!--Copy this boilerplate for easy component building-->
<script setup>
import { gsap } from 'gsap'
import { ref, onMounted } from 'vue'
import Cards from '@/components/Cards.vue'
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import CTAMain from '@/components/CTA-Main.vue'
import Proof from '@/components/Proof.vue'
import Copyright from '@/components/Copyright.vue'
import Socials from '@/components/Socials.vue'
const num_of_questions = ref(6) // This reactive component is used for the description in the header under the header text with class ".info-text".
onMounted(() => {
  const selected_elements = document.querySelectorAll('.show-up') //Loop through each element with the show-up class
  selected_elements.forEach((i) => {
    gsap.from(i, { opacity: 0, y: 20, duration: 1, delay: 0, ease: 'power2.out' })
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
          <span class="show-up h1">Your Skin,</span>
          <span class="force-sameline ws-07 show-up h1">
            Your
            <span class="color-terracotta show-up">Ritual.</span
            ><!--I made sure that the ritual stands out using color-terracotta -->
          </span>
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
        <Cards class="card morning-card show-up" minWidth="150px" minHeight="150px"
          ><!--Morning Routine Card-->
          <span class="time-meridiem">AM</span>
          <div class="card-text-container">
            <span class="fs-2rem">🌅</span>
            <h2 class="card-header">Morning Routine</h2>
            <p class="card-description">Cleanser, Toner, Moisturizer, Sunscreen</p>
          </div>
        </Cards>

        <Cards class="card night-card show-up" minWidth="150px" minHeight="150px"
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
    <div id="steps-container">
      <div>
        <STextLine text="THE PROCESS" class="show-up" />
        <span class="header-text-container">
          <span class="show-up h1">Build Your Routine In</span>
          <span class="force-sameline ws-07 show-up h1">
            Your
            <span class="color-terracotta h1 show-up">3 Steps.</span>
          </span>
        </span>
      </div>
      <div id="steps-wrapper" class="show-up">
        <div class="steps">
          <div class="steps-header-container">
            <h2 class="fs-4rem">❓<!--Image/emoji to represent the card information--></h2>
            <h2 class="color-blush fs-6rem">01<!--Step number--></h2>
          </div>
          <div class="steps-content">
            <h2>Diagnose</h2>
            <p class="card-description">
              Answer a few targeted questions about your skin type, concerns, and daily habits. No
              jargon, just honest answers.
            </p>
          </div>
        </div>
        <div class="steps">
          <div class="steps-header-container">
            <h1 class="fs-4rem">🧪<!--Image/emoji to represent the card information--></h1>
            <h1 class="color-blush fs-6rem">02<!--Step number--></h1>
          </div>
          <div class="steps-content">
            <h2>Match</h2>
            <p class="card-description">
              We match your profile against our curated database of ingredients and formulas, ranked
              by efficacy and compatibility.
            </p>
          </div>
        </div>
        <div class="steps">
          <div class="steps-header-container">
            <h1 class="fs-4rem">✨<!--Image/emoji to represent the card information--></h1>
            <h1 class="color-blush fs-6rem">03<!--Step number--></h1>
          </div>
          <div class="steps-content">
            <h2>Routine</h2>
            <p class="card-description">
              Receive a step-by-step AM/PM routine with product recommendations and guidance on how
              and when to use each one.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>
  <footer>
    <div class="footer-wrapper">
      <!--Copyright component-->
      <Copyright fontSize="0.8rem" />
      <!--Links to privacy Policy, NewsLetter, About and Support-->
      <ul id="footer-links-container">
        <li><RouterLink to="/cookie-policy">Cookie Policy</RouterLink></li>
        <li><RouterLink to="/">Email Reminder</RouterLink></li>
        <li><RouterLink to="/about">About</RouterLink></li>
        <li><RouterLink to="/support">Support</RouterLink></li>
      </ul>
      <!--Social links -->
      <Socials />
    </div>
  </footer>
</template>

<style scoped>
.fs-4rem {
  font-size: 4rem !important;
}
.fs-6rem {
  font-size: 6rem !important;
}
header {
  height: 120vh;
  width: 100%;
  display: flex;
  flex-direction: row;
  position: relative;
  padding: 140px 0 0 0;
  overflow: hidden;
  flex-shrink: 3;
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
  align-items: flex-start;
  flex-shrink: 1;
  overflow-y: auto;
  gap: 40px;
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
  height: auto;
  display: flex;
  flex-shrink: 3;
  flex-direction: column;
  gap: 10px;
}
.header-text-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-shrink: 3;
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
  font-family: 'Playfair Display', sans-serif;
  font-weight: 700;
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
  font-size: 2rem !important;
}
#Main-CTA {
  min-height: auto;
  width: 100%;
  border-radius: 5px;
  padding: 20px;
  background-color: white;
  gap: 10px;
  display: flex;
  flex-shrink: 3;
  flex-direction: column;
  justify-content: space-between;
}
#steps-container {
  width: 100%;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 100px;
  padding: 30px;
  margin-top: 125px;
}
#steps-wrapper {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.color-blush {
  color: var(--blush);
}
.steps {
  background-color: var(--cream);
  min-width: 20%;
  height: 400px;
  border: 1px solid var(--charcoal);
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.steps:hover {
  background-color: var(--warm-white) !important;
  transform: scale(1.008);
}
.steps-header-container {
  width: 100%;
  height: 40%;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
}
.steps-content {
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  gap: 15px;
}
.footer-wrapper {
  width: 100%;
  height: 100px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-end;
}
#footer-links-container {
  width: max-content;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 15px;
  padding: 0 10px; /*y x */
}
#footer-links-container li {
  font-size: 0.8rem;
  color: var(--light-grey);
  list-style: none;
}
#footer-links-container li:hover {
  transform: scale(1.009);
}
#footer-links-container li > a:hover {
  color: var(--terracotta);
}
#footer-links-container a {
  text-decoration: none;
  color: var(--light-grey);
}
@media (max-width: 1024px) {
  header {
    height: auto;
    width: 100%;
    display: flex;
    flex-direction: row;
    position: relative;
    padding: 70px 0 0 0;
    flex-shrink: 3;
  }
  .left-section {
    width: 100%;
    min-height: 1000px;
    display: flex;
    flex-shrink: 3;
    flex-direction: column;
    gap: 30px;
  }
  .header-text-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-shrink: 3;
    gap: 10px;
  }
  .Main-text-container {
    width: 100%;
    height: 40%;
    display: flex;
    flex-shrink: 3;
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
  #steps-wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .steps {
    background-color: var(--cream);
    width: 100%;
    height: 400px;
    border: 1px solid var(--charcoal);
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .footer-wrapper {
    width: 100%;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
  #footer-links-container {
    width: max-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    padding: 0 10px; /*y x */
  }
  .right-section {
    display: none;
  }
}
</style>

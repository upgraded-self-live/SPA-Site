<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import UserQuoteCard from '@/components/UserQuoteCard.vue'
import NoticeDynamic from '@/components/NoticeDynamic.vue'
import DynamicDesignedQuoteCard from '@/components/DynamicDesignedQuoteCard.vue'
import DoubleLinedText from '@/components/DoubleLinedText.vue'
const numOfQuestions = ref(3)
</script>

<template>
  <!--Heading with text saying "Skincare built on You not Trends"-->
  <Navigation />
  <header>
    <div class="left-section">
      <div id="left-section-content">
        <STextLine text="OUR STORY" />
        <span class="h1"
          >Skincare built on <span class="color-terracotta italic">You,</span> not Trends.</span
        >
        <span class="info-text"
          >We started UGRD.LIVE because we were tired of buying products that didn't work. Too many
          brands sell confusion. We sell clarity — a routine that is yours, and yours alone.</span
        >
        <div id="social-testimonies-container">
          <div class="testimony-content">
            <span class="h2 italic"> 2.4<span class="color-terracotta">k+</span></span>
            <span class="info-text"> ROUTINES BUILT</span>
          </div>
          <div class="testimony-content">
            <span class="h2 italic"> 94<span class="color-terracotta">%</span></span>
            <span class="info-text"> SATISFACTION RATE</span>
          </div>
          <div class="testimony-content">
            <span class="h2 italic"> 2<span class="color-terracotta">+</span></span>
            <span class="info-text"> YEARS OF RESEARCH</span>
          </div>
        </div>
      </div>
    </div>
    <div class="right-section">
      <UserQuoteCard
        width="50%"
        height="auto"
        left="20%"
        top="20%"
        name="Ignacious Okpara"
        title="FOUNDER"
        workexperience="SPA/Full-Stack Developer"
        quote="I spent years looking for the right products for my dry skin"
      />
      <UserQuoteCard
        width="50%"
        height="auto"
        left="30%"
        top="60%"
        name="Olajide Olowokere"
        title="CO-FOUNDER"
        workexperience="Python-Developer&UI/UX-Designer"
        quote="Your skin is a priced possession so you have to ensure it keeps its value"
      />
    </div>
  </header>
  <!--sub heading will have a breif description on how I started ugrd.live-->
  <main>
    <section id="our-mission-section">
      <section class="left-section p-top-120 flex-start-al flex-start-just">
        <div id="our-mission-content-wrapper" class="flex-start-al flex-start-just">
          <STextLine text="OUR MISSION" />
          <span class="h2">Why We Built <span class="c-terracotta italic">This</span></span>
          <span class="info-text"
            >The skincare industry has a clarity problem. Shelves are packed with products making
            impossible promises, leaving most people overwhelmed and under-served.</span
          >
          <span class="info-text"
            >We built UGRD.LIVE to cut through the noise — using research-backed matching to connect
            real people with routines that actually work for their skin.</span
          >
          <div class="card-flex-g-20">
            <NoticeDynamic
              title="Evidence First 🧾"
              content="Every product recommendation is backed by peer-reviewed dermatology research, not brand deals."
              backgroundcolor="var(--white)"
              titlecolor="var(--charcoal)"
              infocolor="var(--mid-grey)"
            />
            <NoticeDynamic
              title="Less is More🔬"
              content="We recommend fewer, better products. No 12-step overload. Just what your skin actually needs."
              backgroundcolor="var(--white)"
              titlecolor="var(--charcoal)"
              infocolor="var(--mid-grey)"
            />
            <NoticeDynamic
              title="Radical Transparency🔍"
              content="We tell you exactly why each product is in your routine — ingredient by ingredient."
              backgroundcolor="var(--white)"
              titlecolor="var(--charcoal)"
              infocolor="var(--mid-grey)"
            />
          </div>
        </div>
      </section>
      <section class="right-section">
        <div id="quoteContructor">
          <DynamicDesignedQuoteCard
            quote="Skincare shouldn't require a chemistry degree. It should require knowing yourself."
            author="Ignacious Okpara"
            designonecontent="'IGGY'"
            designtwocontent="'UGRD.LIVE'"
          />
        </div>
      </section>
    </section>
  </main>
  <footer>
    <DoubleLinedText text="Ready" color="var(--light-grey)" linewidth="50" />
    <span class="h1 c-white">Meet Your <span class="italic">Routine</span></span>
    <span class="info-text"
      >{{ numOfQuestions }} questions. 60 seconds. A skincare routine built specifically for your
      skin — no guesswork, no overwhelm.</span
    >
    <div class="button-container">
      <RouterLink to="/quiz"><button class="main-CTA-button">BUILD MY ROUTINE</button></RouterLink>
      <RouterLink to="/support"><button class="secondary-button">SUPPORT</button></RouterLink>
    </div>
  </footer>
</template>

<style scoped>
.h1 {
  font-size: 4rem; /* Made this h1 for the inline span*/
  font-family: 'Playfair Display', sans-serif;
  color: var(--warm-white);
  font-weight: 700;
}
.color-terracotta {
  color: var(--terracotta);
}
.h2 {
  font-size: 3rem; /* Made this h1 for the inline span*/
  font-family: 'Playfair Display', sans-serif;
  color: var(--warm-white);
  font-weight: 600;
}
.italic {
  font-style: italic;
}
header {
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
  position: relative;
  background-image: linear-gradient(110deg, var(--charcoal) 60%, var(--blush-mid) 40%);
  padding: 30px;
}
main {
  overflow-x: hidden;
  width: 100%;
  height: auto;
  position: relative;
  padding: 30px;
}
.left-section {
  width: 50%;
  height: 90%;
  z-index: 4;
}
.right-section {
  width: 50%;
  height: 100vh;
  position: absolute;
  left: 50%;
  top: 0;
  z-index: 5;
  padding: 10px;
}
#left-section-content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
  position: relative;
  top: 20%;
  left: 0;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.1rem;
}
#social-testimonies-container {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0 0 0 30px;
}
.testimony-content {
  width: 120px;
  min-height: 100px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  align-items: center;
}
.testimony-content > span {
  display: block;
  width: 100%;
  height: auto;
}
#our-mission-section {
  width: 100%;
  min-height: 100vh;
  position: relative;
}
#our-mission-section .h1 {
  font-size: 4rem; /* Made this h1 for the inline span*/
  font-family: 'Playfair Display', sans-serif;
  color: var(--charcoal);
  font-weight: 700;
}
#our-mission-section .h2 {
  font-size: 3rem; /* Made this h1 for the inline span*/
  font-family: 'Playfair Display', sans-serif;
  color: var(--charcoal);
  font-weight: 600;
}
#our-mission-content-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 48px;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.1rem;
}
#quoteContructor {
  position: absolute;
  left: 0;
  top: 50%;
  z-index: 1000;
}
footer {
  position: relative;
  margin-bottom: 0;
  width: 100%;
  height: 350px;
  background-color: var(--terracotta);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 30px;
  position: relative;
  overflow: hidden;
}
footer * {
  position: relative;
  overflow: visible;
}
footer span:nth-child(1)::after {
  content: '';
  position: absolute;
  left: 56%;
  top: 13%;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background-color: var(--terracotta-transparent);
}
footer span:nth-child(2)::after {
  content: '';
  position: absolute;
  left: -90%;
  top: -40%;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: var(--terracotta-transparent);
}
footer .info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--light-grey);
  width: 60%;
  font-size: 1.6rem;
  text-align: center;
}
button {
  border: none;
  min-width: 100px;
  height: 50px;
  padding: 10px;
  border-radius: 3px;
}
.button-container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 20px;
}
.main-CTA-button {
  background-color: var(--warm-white);
  color: var(--terracotta);
}
.main-CTA-button:hover {
  transform: translateY(-5px);
  box-shadow: 0px 5px 10px hsla(0, 0%, 26%, 0.5);
}
.secondary-button {
  background: transparent;
  border: 1px solid var(--warm-white);
  color: var(--warm-white);
}
.secondary-button:hover {
  border: 1px solid var(--light-grey);
  color: var(--light-grey);
}
.card-flex-g-20 {
  width: 90%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
button {
  cursor: pointer;
}
</style>

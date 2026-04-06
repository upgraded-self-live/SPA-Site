<!--Copy this boilerplate for easy component building-->
<script setup>
import DoubleLinedText from '@/components/DoubleLinedText.vue'
import PrevRoute from '@/components/PrevRoute.vue'
//form submit function
function submitEmail() {}
</script>

<template>
  <div id="main-container">
    <PrevRoute position="top-left"></PrevRoute>
    <div id="main-wrapper">
      <span class="brand">UGRD.LIVE</span>
      <span class="emoji">🗓️</span>
      <div class="text-container">
        <span class="h2 flex-column"
          >Your monthly<span class="c-terracotta italic">skin check-in.</span></span
        >
        <span class="info-text">
          One email a month. A gentle nudge to revisit your routine, reassess your skin, and stay
          consistent.
        </span>
      </div>

      <form @submit.prevent="submitEmail" class="flex-row-no-g">
        <input type="email" placeholder="your@email.com" required />
        <input type="submit" value="REMIND ME" />
      </form>
      <div class="tags-container">
        <span class="mini-text">Once a month</span>
        <span class="mini-text">No marketting</span>
        <span class="mini-text">Unsubscribe anytime</span>
      </div>
      <DoubleLinedText text="What To Expect" color="var(--light-grey)" linewidth="200" />
      <div class="card-container">
        <span class="c-terracotta mini-text">📬 Example Email — First of Every Month</span>
        <div class="flex-column-start">
          <span class="h6">Your skin this month — time for a check-in?</span>
          <span class="mini-text"
            >Hey — it's been a month since you built your routine. A quick reminder to reassess: has
            your skin changed? Seasonal shifts, stress, and diet all affect it. Tap here to revisit
            your quiz.</span
          >
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#main-container {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
#main-wrapper {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  gap: 30px;
  padding: 10px;
}
.brand {
  font-size: 1rem;
  font-weight: 650;
  font-family: 'Playfair Display', sans-serif;
  color: var(--mid-grey);
}
.emoji {
  font-size: 2rem;
  border-radius: 50%;
  border: 1px solid var(--terracotta);
  padding: 30px;
  position: relative;
}
.emoji::after {
  content: '';
  position: absolute;
  left: -15%;
  top: -13%;
  width: calc(100% + 30px);
  height: calc(100% + 30px);
  border: 1px solid var(--terracotta-light);
  border-radius: 50%;
  opacity: 0.5;
}
.emoji::before {
  content: '';
  position: absolute;
  left: -29%;
  top: -25%;
  width: calc(100% + 60px);
  height: calc(100% + 60px);
  border: 1px solid var(--terracotta-light);
  border-radius: 50%;
  opacity: 0.2;
}
.flex-column {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  gap: 5px;
}
.text-container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
  text-align: center;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 50%;
  font-size: 1.2rem;
  margin-left: 10px;
}
.mini-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--light-grey);
  font-size: 0.6rem;
}
.tags-container {
  width: 100%;
  height: 30px;
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.flex-row-no-g {
  display: flex;
  flex-direction: row;
  gap: 0;
  align-items: center;
}
input {
  height: 60px;
  border: none;
  border-radius: 0;
}
input[type='email'] {
  min-width: 300px;
  padding: 10px;
  outline: 1px solid var(--light-grey);
}
input[type='email']:focus {
  outline: 1px solid var(--terracotta-light);
}
input[type='submit'] {
  min-width: 150px;
  padding: 10px;
  outline: 1px solid var(--light-grey);
  background-color: var(--terracotta);
  color: var(--white);
  cursor: pointer;
}
input[type='submit']:hover {
  background-color: var(--terracotta-dark);
}
.card-container {
  width: 60%;
  height: auto;
  padding: 10px;
  outline: 1px solid var(--light-grey);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}
.flex-column-start {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 5px;
}
</style>

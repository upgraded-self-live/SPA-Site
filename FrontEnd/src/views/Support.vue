<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import { ref } from 'vue'
const formVals = ref({})
const assObj = (objectToAssign, props) => {
  if (typeof objectToAssign != 'object' || typeof props != 'object') {
    throw new console.error('Object expected in arguments')
    return
  }
  Object.assign(objectToAssign, props)
}

function submitEmailForm() {}
</script>

<template>
  <div class="full-body">
    <Navigation />
    <section class="left-section">
      <div class="left-section-wrapper">
        <STextLine text="WE ARE HERE FOR YOU" />
        <span class="h1 c-black">
          What do you need <span class="italic c-terracotta">help</span> with.</span
        >
        <span class="info-text"
          >Send us a quick email of you problem and we will get back right with you.</span
        >
      </div>
      <!--Place mini tags to show perks of our support system like speed-->
      <!--Place footer links such as re-routes-->
    </section>
    <section class="right-section">
      <form @submit.prevent="submitEmailForm">
        <div class="form-element-wrapper">
          <label for="name">Name</label>
          <input
            type="text"
            id="name"
            v-model="formVals.name"
            placeholder="Enter your name"
            required
          />
        </div>
         <div class="form-element-wrapper">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="formVals.email"
            placeholder="Enter your email"
            required
          />
        </div>
        <div class="form-element-wrapper">
          <label for="message">Message</label>
          <textarea
            id="message"
            v-model="formVals.message"
            placeholder="Enter your message"
            required
          ></textarea>
        </div>
           
        <!--Name-->
        <!--Email-->
        <!--Message-->
        <!--Using v-model for value-->
      </form>
    </section>
  </div>
</template>

<style scoped>
.full-body {
  width: 100vw;
  height: 100vh;
  background-color: var(--charcoal);
  display: flex;
  flex-direction: row;
  flex-shrink: 1;
}
.left-section {
  width: 50%;
  height: 100%;
  padding: 30px;
  background-color: var(--blush);
  overflow: hidden;
  position: relative;
  font-weight: 700;
  font-size: 15rem;
  color: var(--terracotta-transparent);
  font-family: 'Playfair Display', sans-serif;
}
.left-section::after {
  content: 'Support';
  position: absolute;
  left: 0;
  top: 50%;
}
.left-section-wrapper {
  width: auto;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
  top: 20%;
  left: 0;
  gap: 20px;
}
.c-black {
  color: var(--charcoal);
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.6rem;
  margin-left: 10px;
  font-weight: 500;
}
</style>

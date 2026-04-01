<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import { ref } from 'vue'
import NoticeDynamic from '@/components/NoticeDynamic.vue'
import ErrorIconSrc from '@/components/Icons/icons8-error-30.png'
import CheckboxIconSrc from '@/components/Icons/icons8-checked-checkbox-30.png'
import { cookieUtils, onUpdate } from '@/Utils'
const formVals = ref({})
const alertRef = ref({
  element: '',
  text: '',
  error: false,
})
const cookieObj = new cookieUtils()
async function submitEmailForm() {
  try {
    if (!cookieObj.getFromCookie('ugrd_contact_limit')) {
       console.log(formVals.value)
    const request = await fetch('http://127.0.0.1:8000/mail', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(formVals.value),
    })
    if (request.ok) {
      const resp = await request.json()
      alertRef.value.text = 'Message has been sent'
      const setContactLimitCookie = cookieObj.setItemInCookie('ugrd_contact_limit',true,(604800*4))
    }
    }
   alertRef.value.error = true;
   alertRef.value.text = 'You recently sent a message please wait for a reply'
  } catch (e) {
    alertRef.value.text = 'An error occurred, please consider sending an email to support@ugrd.live'
    alertRef.value.error = true
    console.error(e)
  }
}
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
          >Send us a quick email of your problem and we will get back right with you.</span
        >
        <div class="flex-column-align-left g-10">
          <NoticeDynamic
            title="Quick response ⏳"
            content="We will respond to you within 3 hours."
            infocolor="var(--light-grey)"
            backgroundcolor="var(--warm-white)"
            titlecolor="var(--terracotta)"
          />
          <NoticeDynamic
            title="We are always open"
            content="We are available 24/7 to support requests."
            infocolor="var(--light-grey)"
            backgroundcolor="var(--warm-white)"
            titlecolor="var(--terracotta)"
          />
          <NoticeDynamic
            title="Mental health support🧠"
            content="We think your mental health is important, feel free to share with us how you feel."
            infocolor="var(--light-grey)"
            backgroundcolor="var(--warm-white)"
            titlecolor="var(--terracotta)"
          />
        </div>
      </div>

      <!--Place mini tags to show perks of our support system like speed-->
      <!--Place footer links such as re-routes-->
    </section>
    <section class="right-section">
      <form @submit.prevent="submitEmailForm" class="right-section-wrapper">
        <div class="form-element-wrapper">
          <label for="name" class="info-text">Name</label>
          <input
            type="text"
            id="name"
            v-model="formVals.name"
            placeholder="Enter your name"
            required
          />
        </div>
        <div class="form-element-wrapper">
          <label for="email" class="info-text">Email</label>
          <input
            type="email"
            id="email"
            v-model="formVals.email"
            placeholder="Enter your email"
            required
          />
        </div>
        <div class="form-element-wrapper">
          <label for="message" class="info-text">Message</label>
          <textarea
            id="message"
            v-model="formVals.message"
            placeholder="Enter your message"
            autocomplete="on"
            required
          ></textarea>
        </div>
        <input type="submit" value="Send" />
        <div class="alert-container" v-if="!alertRef.error && alertRef.text != ''">
          <img :src="CheckboxIconSrc" alt="message sent" />
          <span class="c-white" :ref="alertRef.element">{{ alertRef.text }}</span>
        </div>
        <div class="alert-container" v-if="alertRef.error">
          <img :src="ErrorIconSrc" alt="message failed to send" />
          <span class="c-white" :ref="alertRef.element">{{ alertRef.text }}</span>
        </div>
      </form>
    </section>
    <section class="footer">
      <RouterLink to="/cookie-policy">Cookie Policy</RouterLink>
      <RouterLink to="/">Privacy Policy</RouterLink>
      <RouterLink to="/cookie-policy">Email Reminder</RouterLink>
      <!--Holds routerlinks to privacy policy, cookie policy and Email reminder-->
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
  position: relative;
}
.left-section {
  width: 50%;
  height: 100%;
  padding: 30px;
  background-color: var(--blush);
  overflow: hidden;
  position: relative;
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
.right-section-wrapper {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  gap: 25px;
  flex-shrink: 1;
}
.right-section {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.form-element-wrapper {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}
.form-element-wrapper input[type='text'],
input[type='email'] {
  padding: 5px;
  width: 300px;
  height: 40px;
  border-radius: 5px;
  font-size: 1.3rem;
  border: none;
  outline: none;
  min-width: 100px;
}
.form-element-wrapper input:hover {
  outline: 2px solid var(--terracotta);
}
textarea {
  padding: 10px;
  width: 300px;
  height: 300px;
  border-radius: 5px;
  font-size: 1.3rem;
  border: none;
  outline: none;
  min-width: 100px;
}
textarea:hover {
  outline: 2px solid var(--terracotta);
}
input[type='submit'] {
  border: none;
  border-radius: 5px;
  text-align: center;
  min-width: 100px;
  width: 300px;
  height: 50px;
  font-size: 1.4rem;
  color: var(--white);
  background-color: var(--terracotta);
  cursor: pointer;
}
input[type='submit']:hover {
  background-color: var(--terracotta-dark);
  transform: translateY(-10px);
}
.flex-column-align-left {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.g-10 {
  gap: 10px;
}
.footer {
  position: absolute;
  left: 20px;
  bottom: 0;
  display: flex;
  flex-direction: row;
  gap: 20px;
}
a {
  color: var(--mid-grey);
  position: relative;
  text-decoration: none;
}
.footer a::after {
  content: '';
  width: 5px;
  height: 5px;
  background-color: var(--light-grey);
  border-radius: 50%;
  position: absolute;
  left: -15px;
  top: 25%;
  transform: translateY(50%);
}
.alert-container{
  min-width: 60px;
  min-height: 50px;
  max-width: 90%;
  padding: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  background-color: var(--terracotta);
  border-radius: 10px;
  color: var(--white);
}

@media (max-width: 625px) {
  .full-body {
    width: 100vw;
    height: auto;
    background-color: var(--charcoal);
    display: flex;
    flex-direction: column;
    flex-shrink: 1;
    gap: 120px;
  }
  .left-section {
    width: 100%;
    height: auto;
    padding: 30px;
    background-color: var(--blush);
    overflow: hidden;
    position: relative;
  }
  .left-section-wrapper {
    width: auto;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    top: 20%;
    left: 0;
    gap: 20px;
    text-align: center;
  }
  .right-section {
    width: 100%;
    height: auto;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .right-section-wrapper {
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    gap: 25px;
    position: relative;
    flex-shrink: 1;
    padding: 30px;
  }
  .footer {
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 20px;
  }
  a {
    color: var(--mid-grey);
    position: relative;
    text-decoration: none;
  }
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import Copyright from '@/components/Copyright.vue'
import SocialMedias from '@/components/SocialMedias.vue'
import { ref } from 'vue'
import Error from '@/components/Error.vue'
import { cookieUtils } from '@/Utils'


const errorRef = ref('')
const form = ref({
  name: '',
  email: '',
  message: '',
})
const cookie = new cookieUtils();
async function submit_form() {
  try {
    if (cookie.getFromCookie('contact_form_submitted')) {
      errorRef.value =
        'You have already submitted a message. Please wait for us to get back to you before submitting another.'
      return
    }
    const s = await fetch('http://127.0.0.1:8000/mail', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form.value),
    })
    if (s.ok) {
      errorRef.value = 'Message sent successfully! We will get back to you as soon as possible.'
      cookie.setItemInCookie('contact_form_submitted', true)
      form.value.name = ''
      form.value.email = ''
      form.value.message = ''
    } else {
      alert('Failed to send message. Please try again later.')
    }
  } catch (e) {
    console.error(e)
  }
}
</script>

<template>
  <Navigation class="Navigation" />

  <div class="content-wrapper">
    <Header
      heading="Contact Us"
      subheading="Have a problem with your allocated skincare routine? Send us a message and we will get back to you as soon as possible!"
      imagesrc="/Confused.jpg"
    />
    <form @submit.prevent="submit_form">
      <div class="input-wrapper">
        <span class="label">Name</span>
        <input type="text" name="name" placeholder="Your Name" v-model="form.name" required />
      </div>
      <div class="input-wrapper">
        <span class="label">Email</span>
        <input type="email" name="email" placeholder="Your Email" v-model="form.email" required />
      </div>
      <div class="input-wrapper">
        <span class="label">Message</span>
        <textarea
          name="message"
          placeholder="Your Message"
          v-model="form.message"
          required
        ></textarea>
      </div>
      <button class="submit" type="submit">Send Message</button>
    </form>
    <Error :error="errorRef" class="error-placement" />
    <footer>
      <svg
        data-name="Layer 1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 1200 120"
        preserveAspectRatio="none"
        style="transform: rotate(180deg)"
      >
        <path
          d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
          opacity=".25"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
        <path
          d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
          opacity=".5"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
        <path
          d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
      </svg>
      <ul class="footer-content">
        <li><RouterLink to="/about">About Us</RouterLink></li>

        <li><RouterLink to="/contact">Contact Us</RouterLink></li>

        <li><RouterLink to="/newsletter">Join Our Newsletter</RouterLink></li>
      </ul>
      <Copyright class="copyright" />
      <SocialMedias class="socials" />
    </footer>
  </div>
</template>

<style scoped>
.error-placement {
  margin-top: 30px;
}
.submit {
  width: 100%;
  background-color: #f58598;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  color: white;
}
.submit:active {
  transform: scale(1.009);
  background-color: pink;
}
input {
  padding: 10px;
  border-radius: 5px;
  border: none;
}
textarea {
  max-width: 100%;
  min-height: 200px;
  border: none;
  border-radius: 20px;
  padding: 20px;
}
form {
  border-radius: 20px;
  min-width: 400px;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
  backdrop-filter: blur(50px);
  -webkit-backdrop-filter: blur(50px);
  padding: 20px;
}
.input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 5px;
  width: 100%;
}
.content-wrapper {
  background: transparent;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 125px;
  align-items: center;
}

footer {
  width: 100%;
  height: 500px;
  background: transparent;
  position: relative;
  margin-top: 200px;
  padding: 0;
  margin-bottom: 0;
  overflow: hidden;
}
footer > svg {
  width: 100%;
  position: absolute;
  bottom: 230px;
  left: 0;
}
.footer-content {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 0 !important;
  width: 100%;
  height: 230px;
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-evenly;
  background-color: pink;
}
.footer-content > li {
  list-style: none;
}
.footer-content > li a {
  text-decoration: none;
  color: white;
  font-size: 1.3rem;
}
.socials {
  position: absolute;
  right: 0;
  bottom: 0;
}
.copyright {
  position: absolute;
  left: 10px;
  bottom: 0;
}
</style>

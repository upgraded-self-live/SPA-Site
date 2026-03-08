<!--Copy this boilerplate for easy component building-->
<script setup>
import { cookieUtils, storageUtils } from '@/Utils'
import { onMounted, ref } from 'vue'
import gsap from 'gsap'

const ss = ref(false)
const container = ref()
const cookie = new cookieUtils()
const storage = new storageUtils()

//Check if session storage if not ask
function decline() {
  //session storage
  storage.setItemInSession('cookie_permit', 'blocked')
  ss.value = 'blocked'
}
function accept() {
  //cookie
  cookie.setItemInCookie('cookie_permit', true)
  ss.value = true
}
const check = setInterval(() => {
  try {
    let isallowed = cookie.getFromCookie('cookie_permit')
    if (!isallowed || isallowed === null) {
      ss.value = false
    } else {
      ss.value = isallowed
      if (!container.value) {
        clearInterval(check)
      }
      container.value.remove()
      clearInterval(check)
    }
    isallowed = storage.getItemInSession('cookie_permit')
    if (isallowed === 'blocked') {
      ss.value = 'blocked'
      clearInterval(check)
    }
    ss.value = false
  } catch (e) {
    console.error(e)
    clearInterval(check)
  }
}, 1000)
onMounted(() => {
  gsap.from(container.value, { y: '110%', ease: 'power2.out', duration: 3, delay: 0.3 })
})
</script>

<template>
  <div v-if="ss === false" ref="container" class="container">
    <span
      >Cookies are required for this site to function properly please accept our use of your
      cookies. If you want to know how we use your cookies pleae read our
      <RouterLink to="/">Cookie Usage</RouterLink></span
    >
    <div class="button-container">
      <button @click="accept">Accept</button>
      <button @click="decline">Decline</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  height: 100px;
  border-radius: 30px;
  padding: 20px;
  backdrop-filter: blur(50px);
  -webkit-backdrop-filter: blur(50px);
  background: transparent;
  display: flex;
  flex-direction: row;
  gap: 20px;
  align-items: center;
  justify-content: space-between;
  z-index: 10101010101010;
}
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 110px;
  height: 100%;
  padding: 20px;
}
.button-container > button {
  width: 100%;
  height: 40%;
  border-radius: 30px;
  border: none;
  padding: 10px;
  cursor: pointer;
}
</style>

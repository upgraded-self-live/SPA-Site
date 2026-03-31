<!--Copy this boilerplate for easy component building-->
<script setup>
import FlexSpaceEvenlyContainer from './FlexSpaceEvenlyContainer.vue'
import CTAButton from './CTAButton.vue'
import { onUpdate } from '@/Utils'
import { onMounted, ref } from 'vue'
import sideBarIcon from '@/components/Icons/icons8-sidebar-96.webp'
//check every second if max widhth of the doument is 808px
//I will use window.innerwidth
//Create a button to open the mobile nav
//Make the nav button a global variable
const flexMode = ref('row')
const isMobile = ref(false) //reactive element if it is a mobile screen
const navButtonRef = ref('NOT_ASSIGNED')
const navigation = ref()
function showNav() {
  //Change navigation display to flex
  //This function only runs when navigation button is clicked
  navigation.value.classList.toggle('none')
}
onMounted(() => {
  try {
    onUpdate(() => {
      if (window.innerWidth <= 1024) {
        isMobile.value = true
        flexMode.value = 'column'
        if (!navigation.value?.classList.contains('none')) {
          if (!navButtonRef.value?.classList.contains('nav-open-react')) {
            navButtonRef.value?.classList.add('nav-open-react')
          }
        } else {
          navButtonRef.value?.classList.remove('nav-open-react') //This causes a 'null error' for some reason
        }
      } else {
        flexMode.value = 'row'
        isMobile.value = false
      }
    }, 1000)
  } catch (e) {
    throw new console.error(e)
  }
})
</script>

<template>
  <button v-if="isMobile" id="mobile-nav-button" ref="navButtonRef" @click="showNav">
    <!--Change for a dropdown svg--><img
      :src="sideBarIcon"
      alt="open Side Bar"
      style="width: 40%; height: auto"
    />
  </button>
  <nav ref="navigation">
    <span class="brand">
      <span>UGRD.LIVE</span>
    </span>
    <ul class="Link-Container width-auto">
      <li class="link-wrapper"><RouterLink to="/">HOME</RouterLink></li>
      <li class="link-wrapper"><RouterLink to="/about">ABOUT</RouterLink></li>
    </ul>
    <FlexSpaceEvenlyContainer gap="15px" :direction="flexMode" id="nav-button-container">
      <RouterLink to="/support">
        <button class="contact-button">HAVE A QUESTION?</button>
      </RouterLink>
      <CTAButton />
    </FlexSpaceEvenlyContainer>
  </nav>
</template>

<style scoped>
nav {
  position: fixed;
  top: 0;
  left: 0;
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  width: 100%;
  border-bottom: 1px solid var(--sage);
  height: 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 99999999999;
}
.brand {
  font-family: 'Playfair Display', sans-serif;
  font-size: 1.6rem;
}
.width-auto {
  width: auto;
}
.Link-Container {
  height: 70px;
  display: flex;
  flex-direction: row;
  gap: 20px;
  align-items: center;
}
.Link-Container > li {
  list-style: none;
}
a {
  color: var(--mid-grey);
  text-decoration: none;
}
a:hover {
  color: var(--terracotta-light);
}
button {
  font-family: 'DM Sans', sans-serif;
  min-width: 100px;
  padding: 10px 10px;
  text-align: center;
  cursor: pointer;
}
.contact-button {
  color: var(--mid-grey);
  border: 1px solid var(--mid-grey);
  background: transparent;
}
.contact-button:hover {
  border: 1px solid var(--terracotta);
  color: var(--terracotta);
}

@media (max-width: 1024px) {
  .none {
    display: none !important;
  }
  .nav-open-react {
    background-color: var(--terracotta-dark) !important;
  }
  .brand {
    font-size: 1rem;
    font-family: 'Playfair Display', sans-serif;
  }
  nav button {
    font-family: 'DM Sans', sans-serif;
    width: 100%;
    padding: 10px 10px;
    text-align: center;
    cursor: pointer;
  }
  nav {
    position: fixed;
    top: 0;
    left: 0;
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
    width: 35%;
    border-bottom: 1px solid var(--sage);
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    padding: 0 20px;
    z-index: 99999999999;
  }
  .Link-Container {
    height: 70px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
  }
  #nav-button-container {
    flex-direction: column !important;
  }
  #mobile-nav-button {
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    bottom: 10px;
    left: 50%;
    transform: translateX(-40%) translateY(0);
    z-index: 1000000;
    border-radius: 40px;
    background-color: var(--terracotta);
    color: var(--warm-white);
    border: none;
  }
}
</style>

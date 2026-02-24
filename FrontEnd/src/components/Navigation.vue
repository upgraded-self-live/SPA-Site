<!--Copy this boilerplate for easy component building-->
<script setup>
import { ref } from 'vue'
import Logo100 from './Logo100.vue'

const borderRadius = ref('20px')
</script>

<template>
  <div class="navigation-holder">
    <nav>
      <Logo100 />
      <ul>
        <li class="home"><RouterLink to="/">Home</RouterLink></li>
        <li class="about"><RouterLink to="/">About Us</RouterLink></li>
      </ul>
      <div class="button-container-flex-col">
        <RouterLink to="/"><button class="CTA-button">Build your Routine</button></RouterLink>
        <RouterLink to="/"><button>Have a question?</button></RouterLink>
      </div>
    </nav>
  </div>
</template>

<style scoped>
* {
  transition: all 600ms 1ms ease-in-out;
  box-sizing: border-box;
}
.navigation-holder {
  background: transparent;
  position: fixed;
  top: 0;
  left: 0;
  padding: 10px;
  width: 100vw;
  height: 100px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  z-index: 10000091;
}
nav {
  border-radius: v-bind(borderRadius);
  /*box-shadow: 0 0 10px 0 rgb(68, 67, 67);*/
  background-color: white;
  min-width: 90%;
  min-height: 60px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
nav > ul {
  height: 100%;
  width: 32%;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}
li {
  list-style: none;
  min-width: 100px;
  height: 100%;
  border-radius: v-bind(borderRadius);
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
li:hover {
  transform: scale(1.0009);
  background-color: hsla(0, 9%, 94%, 0.7);
  box-shadow: 0 0 5px 0 rgb(129, 129, 129);
}
a {
  text-decoration: none;
  color: black;
}
.button-container-flex-col {
  min-width: 50px;
  height: 100%;

  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}
button {
  border-radius: v-bind(borderRadius);
  border: none;
  padding: 10px;
  cursor: pointer;
}
button:hover {
  background-color: pink;
}
button:active {
  background-color: rgb(252, 163, 178);
  transform: scale(1.009);
}
</style>

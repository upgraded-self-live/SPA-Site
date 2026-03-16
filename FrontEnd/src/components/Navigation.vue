<!--Copy this boilerplate for easy component building-->
<script setup>
import FlexSpaceEvenlyContainer from './FlexSpaceEvenlyContainer.vue'
import CTAButton from './CTAButton.vue';
</script>

<template>
  <nav>
    <span class="brand">UGRD.LIVE</span>
    <ul class="Link-Container width-auto">
      <li class="link-wrapper"><RouterLink to="/">HOME</RouterLink></li>
      <li class="link-wrapper"><RouterLink to="/">ABOUT</RouterLink></li>
    </ul>
    <FlexSpaceEvenlyContainer gap="15px" direction="row">
      <RouterLink to="/">
        <button class="contact-button">HAVE A QUESTION?</button>
      </RouterLink>
      <CTAButton/>
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
</style>

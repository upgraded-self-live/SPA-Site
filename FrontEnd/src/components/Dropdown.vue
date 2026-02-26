<!--Copy this boilerplate for easy component building-->
<script setup>
import { onMounted, ref, defineProps } from 'vue'
const Props = defineProps(['title', 'dropdownvalue'])
const dropdown = ref(null);
const dropdownVal = ref(null);
function Show() {
  if (!dropdownVal.value) {
    dropdown.value?.querySelector('.dropdownval').classList.toggle('hidden')
    return
  }
  dropdownVal.value?.classList.toggle('hidden')
}
</script>

<template>
  <div class="dropdown" ref="dropdown" @click="Show">
    <span class="title">{{ Props.title }}</span>
    <div class="dropdownval hidden" ref="dropdownVal">{{ Props.dropdownvalue }}</div>
  </div>
</template>

<style scoped>
*::-webkit-scrollbar-button {
  display: none;
}
*::-webkit-scrollbar-thumb {
  display: none;
}
*::-webkit-scrollbar-track {
  display: none;
}
.dropdown {
  width: 99%;
  height: auto;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background-color: white;
  cursor: pointer;
  transition: all 400ms 10ms ease;
}
.title {
  font-size: 1.2rem;
  color: black;
}
.hidden {
  display: none !important;
}
.dropdownval {
  background-color:#E5D9D0;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  display: flex;
  align-items: flex-start;
  width: 98%;
  height: max-content;
  justify-content: center;
  padding: 30px;
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup>
const Props = defineProps({
  quote: {
    type: String,
    default: 'I am a quote card, create a quote attribute to change me :)',
  },
  author: { type: String, default: 'unknown' },
  background: {
    type: String,
    default: 'var(--charcoal)',
  },
  color: {
    type: String,
    default: 'var(--warm-white)',
  },
  designonecontent: { type: String, required: true },
  designtwocontent: { type: String, required: true },
  designonecontentbackgroundcolor: { type: String, default: 'var( --terracotta-transparent)' },
  designtwocontentbackgroundcolor: { type: String, default: 'var( --terracotta-transparent)' },
})
//Add props to accept strings of quotes and names
//Then add design customizations
//Then add color customizaion
</script>

<template>
  <div class="card-container">
    <span id="design-2-holder" class="h3 italic">"{{ Props.quote }}"</span>
    <span class="c-terracotta info-text">-{{ Props.author }}</span>
  </div>
</template>

<style scoped>
.card-container {
  background-color: v-bind(background);
  color: v-bind(color);
  min-width: 80px;
  min-height: 100px;
  border-radius: 10px;
  padding: 34px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px;
  flex-shrink: 3;
  overflow: hidden;
  position: relative;
  font-family: 'Playfair Display', sans-serif;
  font-weight: 700;
}
.info-text {
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
  width: 80%;
  font-size: 1.6rem;
  margin-left: 10px;
}
#design-2-holder {
  position: relative;
}
#design-2-holder::after {
  content: v-bind(designtwocontent);
  color: v-bind(designtwocontentbackgroundcolor);
  position: absolute;
  font-size: 120px;
  width: 30%;
  height: 30%;
  left: 17%;
  bottom: 63%;
}
.card-container::before {
  content: v-bind(designonecontent);
  color: v-bind(designonecontentbackgroundcolor);
  font-size: 100px;
  width: 30%;
  height: auto;
  position: absolute;
  right: 0;
  bottom: -10%;
}
</style>

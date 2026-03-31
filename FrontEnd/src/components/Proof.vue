<!--Copy this boilerplate for easy component building-->
<script setup>
import Star from '@/components/Icons/grey-star-icon.png'
import Glasses from '@/components/Icons/grey-glasses-icon.png'
import Time from '@/components/Icons/grey-time-icon.png'
import NoAccount from '@/components/Icons/grey-no-account-icon.png'
</script>

<template>
  <div class="container">
    <span class="flex-row width-20 height-100 flex-center">
      <!--Icon-->
      <img :src="Star" alt="star icon" class="icon" />
      <span>
        <span class="att"> 4.95/5<!--Grabs the attention of the reader--></span>
        <span class="u-info"> from 2,400 routines built</span>
      </span>
    </span>
    <span class="flex-row mid-grey-left-border width-20 flex-center">
      <!--Icon-->
      <img :src="Glasses" alt="glasses icon" class="icon" />
      <span>
        <span class="att"> Dermatologist reviewed<!--Grabs the attention of the reader--></span>
        <span class="u-info"> product suggestion</span>
      </span>
    </span>
    <span class="flex-row mid-grey-left-border width-20 flex-center">
      <!--Icon-->
      <img :src="Time" alt="time icon" class="icon" />
      <span>
        <span class="u-info">Routine built in </span>
        <span class="att"> under 60 seconds<!--Grabs the attention of the reader--></span>
      </span>
    </span>
    <span class="flex-row flex-center mid-grey-left-border">
      <!--Icon-->
      <img :src="NoAccount" alt="no account icon" class="icon" />
      <span>
        <span class="att"> No account<!--Grabs the attention of the reader--></span>
        <span class="u-info"> required to start</span>
      </span>
    </span>
  </div>
</template>

<style scoped>
* {
  flex-shrink: 1;
}
.container {
  width: 100%;
  height: 120px;
  background-color: var(--charcoal);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  flex-shrink: 2;
}
.flex-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-shrink: 1;
  padding: 0 0 10px 10px;
  gap: 10px;
}
.flex-center {
  align-items: center;
}

.height-100 {
  height: 100%;
}
.att {
  width: inline;
  font-size: 1rem;
  color: var(--warm-white);
}
.u-info {
  width: inline;
  font-size: 0.8rem;
  color: var(--light-grey);
}
.mid-grey-left-border {
  border-left: 1px solid var(--light-grey);
}
.icon {
  width: 24px;
  height: 24px;
  margin-right: 8px;
}
</style>

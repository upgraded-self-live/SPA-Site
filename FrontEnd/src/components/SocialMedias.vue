<!--Copy this boilerplate for easy component building-->
<script setup>
import InstagramIcon from '@/components/Icons/icons8-instagram-120.png'
import TikTokIcon from '@/components/Icons/icons8-tiktok-100.png'
import YoutubeIcon from '@/components/Icons/icons8-youtube-120.png'
</script>

<template>
  <div class="container">
    <a href="https://www.instagram.com/upgraded.self.live/?hl=en" target="_blank"><img :src="InstagramIcon" alt="" /></a>
    <a href="https://www.youtube.com/channel/UCNYPxCKAV-DFXESk3MwaUlg" target="_blank"><img :src="YoutubeIcon" alt="" /></a>
    <a href="https://www.tiktok.com/@upgradedself.live" target="_blank"><img :src="TikTokIcon" alt="" /></a>
  </div>
</template>

<style scoped>
img {
  width: 50px;
  height: 50px;
}
.container {
  min-width: 160px;
  height: 120px;
  padding: 10px;
  background: transparent;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
}
</style>

<!--Copy this boilerplate for easy component building-->
<script setup>
import InstagramIcon from '@/components/Icons/icons8-instagram-120.png'
import TiktokIcon from '@/components/Icons/icons8-tiktok-100.png'
import YoutubeIcon from '@/components/Icons/icons8-youtube-120.png'
</script>

<template>
  <div class="social-media-container">
    <a href="https://www.tiktok.com/search?q=upgradedself.live&t=1772989192571" target="_blank"
      ><img :src="TiktokIcon" alt="" class="icon"
    /></a>
    <a href="  https://www.instagram.com/upgraded.self.live/?hl=en" target="_blank"
      ><img :src="InstagramIcon" alt="" class="icon"
    /></a>
    <a href="https://www.youtube.com/@UpgradedSelf_live" target="_blank"><img :src="YoutubeIcon" alt="" class="icon" /></a>
  </div>
</template>

<style scoped>
.social-media-container {
  width: max-content;
  height: 100px;
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: flex-end;
}
.icon {
  width: 30px;
  height: auto;
}
</style>

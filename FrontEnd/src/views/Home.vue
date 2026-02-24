<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import VerticalCard from '@/components/VerticalCard.vue'
</script>

<template>
  <div class="content-wrapper">
    <Navigation class="Navigation" />
    <Header
      heading="Get Proven Skincare Routine in 60 Seconds"
      subheading="Built on countless research and reviews from users across the web."
      imagesrc="src/assets/Header-image-1.jpg"
    />
    <div class="full-width blur skin-types">
      <div class="text-wrapper"></div>
      <div class="grid2x2 skin-types-wrapper"></div>
    </div>
    <div class="card-container-flex-horziontal">
      <VerticalCard
        imgsrc="src/assets/Skincare-products-1.jpg"
        heading="Buy What You Need"
        text="Don't overspend on products you don't need."
      />
      <VerticalCard
        imgsrc="src/assets/Verified-pink.png"
        heading="Get Products That Work"
        text="Products are selected from valuable research and reviews."
      />

      <VerticalCard
        imgsrc="src/assets/Routinethatworksimage-1.jpg"
        heading="Clear & Simple"
        text="No fluff, no nonsense, a clear routine for your skin type."
      />
    </div>

    <div class="full-background Quote-container">
      <span class="italic fs-50 quote fw-700">"The best wrinkle is the one you never get."</span>
    </div>
  </div>
</template>

<style scoped>
.quote {
  text-align: center;
  color: white;
}
.Quote-container {
  position: relative;
  width: 99%;
  min-height: 100px;
  top: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px;
}
.full-background {
  background-color: pink;
}
fw-700 {
  font-weight: 700;
}
.fs-50 {
  font-size: 50px;
}
.italic {
  font-style: italic;
}

.Navigation:deep(.home) {
  transform: scale(1.0009);
  background-color: hsla(0, 9%, 94%, 0.7);
}
.content-wrapper {
  background: transparent;
  position: relative;
  width: 100%;
  height: 100vh;
}
.card-container-flex-horziontal {
  position: relative;
  top: 70px;
  width: 95%;
  min-height: 250px;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  padding: 20px;
}
</style>

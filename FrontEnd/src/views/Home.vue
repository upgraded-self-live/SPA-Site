<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import VerticalCard from '@/components/VerticalCard.vue'
import TextDivWithArrow from '@/components/TextDivWithArrow.vue'
import CTAbutton from '@/components/CTAbutton.vue'
import Section from '@/components/Section.vue'
import CTA from '@/components/CTA.vue'
import Dropdown from '@/components/Dropdown.vue'
</script>

<template>
  <div class="content-wrapper">
    <Navigation class="Navigation" />
    <Header
      heading="Get Proven Skincare Routine in 60 Seconds"
      subheading="Built on countless research and reviews from users across the web."
      imagesrc="src/assets/Header-image-1.jpg"
    />
    <Section
      title="Get a Skincare Routine gauranteed to work for your skin type"
      subtitle="If your allocated skincare routine does'nt work in 4 months, feel free to contact us."
    />
    <div class="full-width blur skin-types">
      <div class="text-wrapper">
        <span class="fs-50 fw-700">Find Your Skin Type</span>
        <span class="fs-20">Not sure about your skin type? Take our quiz to find out.</span>
        <CTAbutton />
      </div>
      <div class="grid2x2 skin-types-wrapper">
        <TextDivWithArrow
          text="Oily Skin"
          src="src/assets/Oily-skin.webp"
          href="https://www.google.com/search?q=what+is+oily+skin"
        />
        <TextDivWithArrow
          text="Dry Skin"
          src="src/assets/Dry-skin.webp"
          href="https://www.google.com/search?q=what+is+dry+skin"
        />
        <TextDivWithArrow
          text="Combination Skin"
          src="src/assets/Combination-skin.webp"
          href="https://www.google.com/search?q=what+is+combination+skin"
        />
      </div>
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
    <!--I will talk about how their skin is our priority-->
    <Section
      title="Your Skin is Our Priority"
      subtitle="Our main focus is to ensure you get the best version of your skin. We are committed to providing you with the best skincare routine that suits your skin type and concerns."
    />
    <CTA />
    <Section
      title="Improve facial attraction"
      subtitle="Skincare is not just about health, it's also about improving your facial attraction. A good skincare routine can enhance your natural beauty and boost your confidence."
      img="src/assets/alehidalgo-model-429733_1280.jpg"
    />

    <div class="full-width FAQ-container">
      <span class="title">FAQ</span>
      <div class="FAQ-dropdown-container">
        <Dropdown
          title="'What do we do if we have normal skin?'"
          dropdownvalue="Having normal skin is very rare but if you have normal skin you do not have to use a skin care routine, but if 
        you want to look better then we recommend you use a cleanser > toner > retinol > peptides > moisturizer > sunscreen."
        />
        <Dropdown
          title="'Is our skincare effective?'"
          dropdownvalue="Our skincare routine is built on countless research and reviews from users across the web. We are confident that our skincare routine will work for you, but if it doesn't work in 4 months, feel free to contact us."
        />
        <Dropdown
          title="'How often should I wash my face?'"
          dropdownvalue="Most people should cleanse:

Twice daily (morning and night)

After heavy sweating

Over-cleansing can damage your skin barrier and cause dryness or irritation."
        />
        <Dropdown
          title="'Do I really need sunscreen every day?'"
          dropdownvalue="Yes. Daily sunscreen protects against:

Premature aging

Hyperpigmentation

Sun damage

Skin cancer

Even on cloudy days, UV rays can affect your skin. Use at least SPF 30."
        />
        <Dropdown
          title="'Can I use multiple active ingredients together?'"
          dropdownvalue="Some ingredients pair well, others don’t.

Safe combinations:

Vitamin C + SPF

Hyaluronic Acid + almost anything

Niacinamide + most ingredients

Use caution when combining:

Retinol + AHAs/BHAs

Strong exfoliants together

If unsure, introduce one active at a time."
        />
        <Dropdown
          title="'Why is my skin breaking out after starting a new product?'"
          dropdownvalue="This could be:

Purging (temporary breakout due to active ingredients)

Or irritation/reaction

Purging usually happens with exfoliating or cell-turnover ingredients and improves within 4–6 weeks.

If irritation persists, discontinue use."
        />
      </div>
    </div>
    <footer>
      <svg
        data-name="Layer 1"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 1200 120"
        preserveAspectRatio="none"
        style="transform: rotate(180deg)"
      >
        <path
          d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
          opacity=".25"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
        <path
          d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
          opacity=".5"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
        <path
          d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
          class="shape-fill"
          fill="#FFC0CB"
          fill-opacity="1"
        ></path>
      </svg>
      <div class="footer-content"></div>
    </footer>
  </div>
</template>

<style scoped>
footer {
  width: 100%;
  min-height: 300px;
  background: transparent;
  position: relative;
  margin-top: 300px;
}
footer > svg {
  width: 100%;
  position: absolute;
  bottom: 99%;
  left: 0;
}
.footer-content {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 300px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  background-color: pink;
}
.content-wrapper {
  background: transparent;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 125px;
  align-items: center;
}
.top-200 {
  position: relative;
  top: 200px !important;
}
.FAQ-container > .title {
  font-size: 3rem;
  font-weight: 700;
  color: black;
}
.FAQ-container {
  min-height: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
.skin-types {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 50px;
  position: relative;
  top: 0;
}
.grid2x2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
.text-wrapper {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
.FAQ-dropdown-container {
  width: 100%;
  height: auto;
  border-radius: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: hsla(0, 0%, 100%, 0.7);
  overflow: hidden;
}
.fs-20 {
  font-size: 20px;
}
.blur {
  backdrop-filter: blur(50px);
  -webkit-backdrop-filter: blur(50px);
}
.quote {
  text-align: center;
  color: white;
}
.Quote-container {
  position: relative;
  width: 99%;
  min-height: 100px;
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
  background-color: #e5d9d0;
}

.card-container-flex-horziontal {
  position: relative;
  top: 0;
  width: 95%;
  min-height: 350px;
  overflow-y: hidden;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  padding: 20px;
}
.full-width {
  width: 100%;
}
</style>

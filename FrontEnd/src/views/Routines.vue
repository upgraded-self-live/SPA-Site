<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import Section from '@/components/Section.vue';
import CTA from '@/components/CTA.vue'
</script>

<template>
  <div class="content-wrapper">
    <Navigation />
    <Header
      heading="Know Why a Skincare Routine is Important"
      subheading="We will share with you all our research on the importance of skincare skincare routines."
      imagesrc="/hermann-books-5937823_1280.jpg"
    />
    <Section title="What is your skin?" subtitle="Lets start with the basics. Your skin is the largest and thickest organ on the body acting as a barrier against pathogens, UV light, and injury, but this does'nt mean the skin is great at its job, this is where a skincare routine comes in and support the skin to complete its function by providing the nutrients it needs to look and stay healthy. The thickness of the body varies depending on the age and gender of the person. There are also different skin types such as dry skin, oily skin, combination skin (T-zone and U zone) and sensitive skin. We will cover how to detect each skin type next." img="/marcodamoda-face-5903577_1280.jpg"/>
    <!--Start with the basics of human skin and how dirt forms-->
    
    <!--Advantages of a healthy skin-->
     <Section title="Why have a healthy and smooth skin" subtitle="
     Having a smooth and healthy skin may impact your confidence, how people initially percieve you and may improve self love but it's not just about aesthetics, it also has many health benefits. A healthy skin can protect you from: harmful UV rays, prevent infections, and even boost your confidence. A good skincare routine can help you achieve and maintain a healthy skin by providing it with the necessary nutrients and hydration it needs to function properly as a result you experience less wrinkles, eye bags, less visible pores and a more younger look. You will finally be able to look good in photos."
     " img="/whitedaemon-girl-2771001_1280.jpg"/>
    <!--Factors of a healthy skin-->
     <Section title="Factors of a Healthy skin" subtitle="
     In order to achieve a healthy or 'glass skin' might sound quite complicated but it is actully not, it is a mix of intense moisturization, cleansing and quite fine amount of treatment products. for example

    Hyaluronic Acid: A potent humectant that draws moisture into the skin, plumping it up and giving it a bouncy, dewy texture.
    Niacinamide (Vitamin B3): Repairs the skin barrier, reduces inflammation, and refines the appearance of pores.
    Vitamin C: Brightens skin, treats hyperpigmentation, and promotes collagen production.
    Ceramides: Crucial for lipid restoration and maintaining the structural integrity of the skin barrier.
    Double Cleansing: Using an oil-based cleanser followed by a water-based one to completely remove makeup, sunscreen, and pollutants, preventing clogged pores and dullness.
    Peptides: Short chains of amino acids that act as messengers, signalling fibroblasts to produce more collagen, elastin, and hyaluronic acid.
    Retinoids (Vitamin A): Considered the 'gold standard' for anti-aging, these stimulate fibroblast collagen production, accelerate cell turnover, and reduce fine lines but. there some drawbacks to using this.
     "
      />
        <Section title="Skin types" subtitle="
    Not everyone has the same skin type, this is due to either genetics or evolutionary adaptation to environmental UV radiations.
    Dry skins typically known as xerosis, are due to the skin having a weak barrier and low water retention (hydration) capabilities, this can be caused by genetics, environmental factors such as cold weather, or even harsh skincare products. Dry skins are typically prone to itching and flaking normally after showers. Oily skin is caused by an overproduction of sebum, which can lead to clogged pores and acne. Combination skin is a mix of both dry and oily skin, with the T-zone (forehead, nose, and chin) being oily and the U-zone (cheeks and jawline) being dry. Sensitive skin is characterized by redness, itching, and irritation, and can be caused by a variety of factors such as genetics, environmental factors, or even certain skincare products. It is important to identify your skin type in order to choose the right skincare products and routine for your specific needs but don't worry we will handle that part for you.
     "
      />
    <!--How some products may damage the user's skin-->
         <Section title="How skincare brands take advantage of you" subtitle="
    Some skincare brands do not work nor care about your skin, all they care about is the profit and presentation of the product some of them consist of random nutrients and chemicals that are not even supposed to be on your skin, they take advantage of your lack of knowledge and your insecurities to make you buy their products, they use marketing strategies to make you think that you need their products to look good and be healthy but in reality, you don't need most of the products they sell, you just need a good routine that is suitable for your skin type and that is what we will provide you with.
     "
      />
    <!--Go on to each step of a good routine-->
    <!--Might include night routines-->
     <CTA />
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
          <ul class="footer-content">
            <li><RouterLink to="/about">About Us</RouterLink></li>
    
            <li><RouterLink to="/contact">Contact Us</RouterLink></li>
    
            <li><RouterLink to="/newsletter">Join Our Newsletter</RouterLink></li>
          </ul>
          <Copyright class="copyright" />
          <SocialMedias class="socials" />
        </footer>
  </div>
</template>

<style scoped>
.Navigation:deep(.routine) {
  transform: scale(1.0009);
  background-color: #e5d9d0;
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
}footer {
  width: 100%;
  height: 500px;
  background: transparent;
  position: relative;
  margin-top: 200px;
  padding: 0;
  margin-bottom: 0;
  overflow: hidden;
}
footer > svg {
  width: 100%;
  position: absolute;
  bottom: 230px;
  left: 0;
}
.footer-content {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 0 !important;
  width: 100%;
  height: 230px;
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-evenly;
  background-color: pink;
}
.footer-content > li {
  list-style: none;
}
.footer-content > li a {
  text-decoration: none;
  color: white;
  font-size: 1.3rem;
}
</style>

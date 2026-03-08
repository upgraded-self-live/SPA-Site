<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import Section from '@/components/Section.vue'
import Copyright from '@/components/Copyright.vue'
import SocialMedias from '@/components/SocialMedias.vue'
</script>

<template>
  <Navigation class="Navigation" />

  <div class="content-wrapper">
    <Header
      heading="Learn More About Our Mission"
      subheading="Know why we exist and what we're trying to accomplish."
      imagesrc="/About-Us-Header-photo.jpg"
    />
    <Section
      title="Our Mission"
      subtitle="I created this platform to simplify skincare decisions and help people find a skincare product for their skin type."
    />
    <Section
      title="My Story"
      subtitle="As someone with severe dry skin who struggled with finding the right product for their skin type, I created this platform to help others avoid the same mistakes. By giving products that actually work and avoid over-spending like I did. Our product recommendations are research backed and based on real user reviews, so you can trust that you're getting the best advice for your skin and budget."
    />
    <Section
      title="How We Recommend Products to You"
      subtitle="We ask you questions regarding your gender and skin type, and then we use an algorithm to recommend products that are suitable for you. We also provide you with a routine that you can follow to achieve the best results. We get a commision anytime you buy the products so this helps us maintain this platform, pay our creators and keep it free for everyone. Please know that we are available if a product causes you any irritation or if you have any questions regarding the products or your routine."
    />
    <Section
      title="Our Values"
      subtitle="We aim to provide the best skincare advice and products for everyone, regardless of their budget or skin type. We believe that everyone deserves to have healthy and beautiful skin, and we are committed to helping our users achieve that. We also value transparency and honesty, and we strive to provide our users with accurate and unbiased information about skincare products."
    />
    <Section
      title="About Me"
      subtitle="I am a full-stack developer and skincare enthusiast passionate about helping people find the right products for their skin and solving problems that I have personally faced."
    />
    <Section
      title="Disclaimer"
      subtitle="Please note that the products we recommend are not guaranteed to work for everyone, as everyone's skin is different. We recommend that you do your own research and consult with a dermatologist before trying any new products, especially if you have sensitive skin or any skin conditions."
    />
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
.Navigation:deep(.about) {
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
}

footer {
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
.socials {
  position: absolute;
  right: 0;
  bottom: 0;
}
.copyright {
  position: absolute;
  left: 10px;
  bottom: 0;
}
</style>

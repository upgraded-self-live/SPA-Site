<!--Copy this boilerplate for easy component building-->
<script setup>
import Navigation from '@/components/Navigation.vue'
import STextLine from '@/components/STextLine.vue'
import Copyright from '@/components/Copyright.vue'
import { ref } from 'vue'
import Notice from '@/components/Notice.vue'
const websiteName = ref('upgradedself.live')
</script>

<template>
  <Navigation />
  <div id="sidebar">
    <span class="brand">UGRD.LIVE</span>
    <ul class="page-links">
      <li><a href="#section-01">Section 1: What is are cookies🍪?</a></li>
      <li><a href="#section-02">Section 2: How we use cookies</a></li>
      <li><a href="#section-03">Section 3: Types of cookies we use</a></li>
      <li><a href="#section-04">Section 4: Contact us </a></li>
      <!--This will contain links to different sections of the document-->
    </ul>
    <Copyright class="abs-bottom" />
  </div>
  <div class="content">
    <section>
      <div class="section-header">
        <STextLine text="LEGAL" class="show-up" />
        <span class="h1">Cookie <span class="color-terracotta h1 show-up">Policy</span></span>
      </div>
      <div class="section-content">
        <p>
          This policy explains clearly what cookies {{ websiteName }} uses and why we create them.
          This document is written in plain english.
        </p>
      </div>
    </section>
    <!--Section 01-->
    <section>
      <div class="section-header">
        <STextLine text="SECTION 01" class="show-up" id="section-01" />
        <span class="h1">What Are <span class="color-terracotta h1 show-up">Cookies</span></span>
      </div>
      <div class="section-content">
        <p>
          Cookies are small text files placed on your device when you visit a website. They're used
          to remember your preferences, understand how you use a site, and in some cases to show you
          relevant advertising. They don't contain personal information on their own, but they can
          be linked to it.
        </p>
        <p>
          {{ websiteName }} uses cookies to make your experience better — primarily to remember your
          quiz progress and your quiz result (Your designated routine.)
        </p>

        <Notice
          title="Our Approach"
          content="We try our best to use as minimal cookies as possible. We do not sell data collected via our cookies and we never will."
        />
      </div>
    </section>

    <!--Section 02-->
    <section>
      <div class="section-header">
        <STextLine text="SECTION 02" class="show-up" id="section-02" />
        <span class="h1">How We Use <span class="color-terracotta h1 show-up">Cookies</span></span>
      </div>
      <div class="section-content">
        <p>
          We use cookies for three main purposes: to keep our site working correctly, to understand
          how visitors use it so we can improve it, and to remember your skin quiz progress and
          preferences between sessions.
        </p>
        <p>
          We do not use cookies to build advertising profiles, track you across other websites, or
          share data with social media platforms without your explicit consent.
        </p>
      </div>
    </section>
    <!--Section 03-->
    <section>
      <div class="section-header">
        <STextLine text="SECTION 03" class="show-up" id="section-03" />
        <span class="h1"
          >Types Of <span class="color-terracotta h1 show-up">Cookies</span>
          <span class="h1">We Use</span></span
        >
      </div>
      <div class="section-content">
        <p>
          This section will contain all the cookies used by {{ websiteName }} in the form of a table
          containing: "name", "purpose" and "duration".
        </p>
        <table class="cookie-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Purpose</th>
              <th>Duration</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>ugrd_session</td>
              <td>Stores your quiz progress and preferences</td>
              <td>60 minutes</td>
            </tr>
            <tr>
              <td>ugrd_result</td>
              <td>Stores the result of your quiz like routines and product recommendation</td>
              <td>1 month</td>
            </tr>
            <tr>
              <td>ugrd_contact_limit</td>
              <td>Stores if you (user) have recently sent a question, this is to stop spammers.</td>
              <td>24 hours</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
    <section id="section-04">
      <div id="contact-container">
        <div class="contact-header">
          <span class="contact-title">Contact Us</span>
        </div>
        <div class="contact-content">
          <span class="contact-text"
            >If you have any questions please don't hesitate to contact us, we typically answer
            within a day.
          </span>
        </div>
        <div class="button-container-row">
          <RouterLink to="/"><button class="primary-button">CONTACT US</button></RouterLink>
          <RouterLink to="/"
            ><button class="secondary-button">BUILD YOUR ROUTINE</button></RouterLink
          >
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
#sidebar {
  position: fixed;
  left: 0;
  z-index: 100;
  background-color: var(--charcoal);
  padding: 10px;
  width: 30%;
  height: 100%;
}
.section-content {
  width: 100%;
  min-height: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 25px;
}
section {
  width: 100%;
  min-height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  gap: 40px;
  margin-top: 100px;
}
.section-header {
  width: 100%;
  height: 70px;
}
.content {
  width: 70%;
  height: 100%;
  position: fixed;
  right: 0;
  top: 100px;
  z-index: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0 120px 120px 120px;
  gap: 100px;
}
.brand {
  font-family: 'Playfair Display', serif;
  color: var(--warm-white);
  font-size: 1.6rem;
  width: 100%;
  position: absolute;
  top: 15%;
  left: 20px;
}
.page-links {
  width: 100%;
  height: auto;
  position: absolute;
  top: 25%;
  left: 0;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.page-link li {
  list-style: none;
}
.page-links a {
  color: var(--warm-white);
}
.color-terracotta {
  color: var(--terracotta-dark);
}
.h1 {
  font-size: 3rem; /* Made this h1 for the inline span*/
  font-weight: 700;
  font-family: 'Playfair Display', sans-serif;
}
.abs-bottom {
  position: absolute;
  bottom: 10px;
}
p {
  font-size: 1rem;
  font-family: 'DM Sans', sans-serif;
  color: var(--mid-grey);
}
cookie-table {
  width: 100%;
  border-collapse: collapse; /* removes gaps between cell borders */
}

.cookie-table th {
  background: var(--charcoal);
  color: white;
  padding: 12px 16px;
  text-align: left;
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.cookie-table thead tr :nth-child(1) {
  border-top-left-radius: 10px;
}
.cookie-table thead tr :nth-child(3) {
  border-top-right-radius: 10px;
}
.cookie-table td {
  padding: 14px 16px;
  border-bottom: 1px solid var(--light-grey);
  font-size: 14px;
  color: var(--mid-grey);
}

/* Zebra striping for readability */
.cookie-table tbody tr:nth-child(even) td {
  background: var(--warm-white);
}
#contact-container {
  width: 100%;
  min-height: 150px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 30px;
  background-color: var(--charcoal);
  border-radius: 10px;
  padding: 10px;
}
.contact-header {
  width: 100%;
  text-align: left;
}
.contact-title {
  font-size: 1.2rem;
  color: var(--warm-white);
  font-weight: 600;
  font-family: 'Playfair Display', sans-serif;
  letter-spacing: 2px;
}
.contact-text {
  color: var(--light-grey);
  font-size: 0.9rem;
  color: var(--warm-white);
  font-weight: 500;
}
.button-container-row {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 10px;
}
button {
  height: 45px;
  min-width: 60px;
  border-radius: 5px;
  padding: 15px;
  border: none;
  cursor: pointer;
}
.primary-button {
  background-color: var(--terracotta);
  color: var(--warm-white);
}
.primary-button:hover {
  background-color: var(--terracotta-dark);
  transform: translateY(-5px);
}
.secondary-button {
  background-color: var(--charcoal);
  color: var(--warm-white);
}
.secondary-button:hover {
  background-color: var(--mid-grey);
  color: var(--warm-white);
}
</style>

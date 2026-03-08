import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Contact from '@/views/Contact.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Routine from '@/views/Routines.vue'
import Newsletter from '@/views/Newsletter.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: Home, meta: { title: 'UpgradedSelf.live| Home' } },
    {
      path: '/about',
      name: 'about',
      component: About,
      meta: { title: 'UpgradedSelf.live| About' },
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact,
      meta: { title: 'UpgradedSelf.live| Contact Us' },
    },
    {
      path: '/newsletter',
      name: 'newsletter',
      component: Newsletter,
      meta: { title: 'UpgradedSelf.live| NewsLetter' },
    },
    {
      path: '/routines',
      name: 'routines',
      component: Routine,
      meta: { title: 'UpgradedSelf.live| Routines' },
    },
  ],
})
router.beforeEach((to) => {
  document.title = to.meta?.title
})
export default router

import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import CookiePolicy from '@/views/CookiePolicy.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: Home, meta: { title: 'UpgradedSelf.live| Home' } },
    { path: '/cookie-policy', name: 'cookiePolicy', component: CookiePolicy, meta: { title: 'UpgradedSelf.live| CookiePolicy' } },
  ],
})
router.beforeEach((to) => {
  document.title = to.meta?.title
})
export default router

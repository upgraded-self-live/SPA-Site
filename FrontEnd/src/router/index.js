import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue'),
      meta: { title: 'Build Your Skincare Routine | UpgradedSelf.live' },
    },
    {
      path: '/cookie-policy',
      name: 'cookiePolicy',
      component: () => import('@/views/CookiePolicy.vue'),
      meta: { title: 'Cookie Policy | UpgradedSelf.live' },
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/About.vue'),
      meta: { title: 'About | UpgradedSelf.live' },
    },
    {
      path: '/support',
      name: 'support',
      component: () => import('@/views/Support.vue'),
      meta: { title: 'Support | UpgradedSelf.live' },
    },
  ],
})
router.beforeEach((to) => {
  document.title = to.meta?.title
})
export default router

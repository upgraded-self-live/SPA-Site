import Home from '@/views/Home.vue';
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
   {path: '/', name: 'home', component: Home, meta: {title: 'UpgradedSelf.live| Home'}}
  ],
})
router.beforeEach(to => {
  document.title = to.meta?.title;
})
export default router

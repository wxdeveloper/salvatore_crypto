import { createRouter, createWebHistory, createMemoryHistory } from 'vue-router'

import MainPage from '../components/MainPage.vue'
import Services from '../components/Services.vue'

const routes = [
  { path: '/', component: MainPage },
  { path: '/services', component: Services}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;




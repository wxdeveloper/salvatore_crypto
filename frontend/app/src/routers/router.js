import { createRouter, createWebHistory, createMemoryHistory } from 'vue-router'

import MainPage from '../components/MainPage.vue'
import Stargaze from '../components/Stargaze.vue'

const routes = [
  { path: '/', component: MainPage },
  { path: '/stargaze', component: Stargaze}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;




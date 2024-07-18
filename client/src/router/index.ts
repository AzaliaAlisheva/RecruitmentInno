import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import SpecialistsMatching from '../views/SpecialistsMatching.vue'
import SpecDescription from '../views/SpecDescription.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,

  },
  {
    path: '/vacancies/:id/',
    name: 'Specialists',
    component: SpecialistsMatching,
    props: true,
  },
  {
    path: '/specialists/:id/',  
    name: 'SpecialistDescription',
    component: SpecDescription,
    props: true, 
  },
  // {
  //   path: '/signup',
  //   name: 'SignUp',
  //   component: SignUpView,
  // },
  // {
  //   path: '/login',
  //   name: 'LogIn',
  //   component: LogInView
  // },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router;

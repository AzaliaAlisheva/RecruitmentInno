import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeP from '../views/HomeP.vue'
import SpecialistsMatching from '../views/SpecialistsMatching.vue'
import SpecDescription from '../views/SpecDescription.vue'
import AboutView from '../views/AboutView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeP
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/vacancies/:id/',
    name: 'Specialists',
    component: SpecialistsMatching,
    props: true
  },
  {
    path: '/vacancies',
    name: 'HomeView',
    component: HomeView,
    props: true
  },
  {
    path: '/specialists/:id/',  
    name: 'SpecialistDescription',
    component: SpecDescription,
    props: true, 
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router;

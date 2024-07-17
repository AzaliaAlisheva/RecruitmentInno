import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import SpecialistsMatching from '../views/SpecialistsMatching.vue'
import SpecDescription from '../views/SpecDescription.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { requiresAuth: true },

  },
  {
    path: '/vacancies/:id/',
    name: 'Specialists',
    component: SpecialistsMatching,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: '/specialists/:id/',  
    name: 'SpecialistDescription',
    component: SpecDescription,
    props: true, 
    meta: { requiresAuth: true },
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogInView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated'); 

  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'LogIn' });
  } else {
    next();
  }
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated'); 

  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'LogIn' });
  } else {
    next();
  }
});

export default router;

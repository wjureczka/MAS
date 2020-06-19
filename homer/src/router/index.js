import Vue from 'vue'
import VueRouter from 'vue-router'
import { authGuard } from '@/utils'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path: '/groups',
    name: 'Groups',
    component: () => import(/* webpackChunkName: "about" */ '../views/Groups.vue'),
    beforeEnter: authGuard
  },
  {
    path: '*',
    name: 'Not found',
    component: () => import(/* webpackChunkName: "about" */ '../views/NotFound.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

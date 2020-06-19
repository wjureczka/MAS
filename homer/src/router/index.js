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
    path: '/groups/new-group-form',
    name: 'New group form',
    component: () => import(/* webpackChunkName: "about" */ '../views/NewGroupForm.vue'),
    beforeEnter: authGuard
  },
  {
    path: '/groups/:id/group-created',
    name: 'Group created',
    props: true,
    component: () => import(/* webpackChunkName: "about" */ '../views/GroupCreated.vue'),
    beforeEnter: authGuard
  },
  {
    path: '/groups/:id/add-user',
    name: 'Add user to group',
    props: true,
    component: () => import(/* webpackChunkName: "about" */ '../views/GroupAddUser.vue'),
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

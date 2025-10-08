/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

import { setupLayouts } from 'virtual:generated-layouts'
// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
// import { routes } from 'vue-router/auto-routes'
import UserData from '@/pages/UserData.vue'
import Dashboard from '@/pages/Dashboard.vue'
import Alternative from '@/pages/Alternative.vue'
import Criteria from '@/pages/Criteria.vue'
import Profile from '@/pages/Profile.vue'
import Ranking from '@/pages/Ranking.vue'
import MatriksData from '@/pages/MatriksData.vue'
import index from '@/pages/index.vue'
import ScoringData from '@/pages/ScoringData.vue'
import TopsisScore from '@/pages/TopsisScore.vue'
import path from 'path'
import { components } from 'vuetify/lib/labs/entry-bundler.mjs'

const routes = [
  {
    path: '/',
    name: 'login',
    component: index,
  },
  {
    path: '/dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }, // semua user bisa akses
  },
  {
    path: '/alternative',
    component: Alternative,
    meta: { requiresAuth: true }, // semua user bisa akses
  },
  {
    path: '/userdata',
    component: UserData,
    meta: { requiresAuth: true, role: 'admin' }, // hanya admin
  },
  {
    path: '/criteria',
    component: Criteria,
    meta: { requiresAuth: true },
  },
  {
    path: '/ranking',
    component: Ranking,
    meta: { requiresAuth: true },
  }
  ,
  {
    path: '/topsisscore',
    component: TopsisScore,
    meta: { requiresAuth: true },
  }
  ,
  {
    path: '/profile',
    component: Profile,
    meta: { requiresAuth: true },
  }
  ,
  {
    path: '/matriksdata',
    component: MatriksData,
    meta: { requiresAuth: true },
  }
  ,
  {
    path: '/scoringdata',
    component: ScoringData,
    meta: { requiresAuth: true },
  }
  
]

// const enhancedRoutes = setupLayouts(routes) // bisa tambahkan layout

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(routes),
  linkActiveClass: 'border-red-200',
})

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (localStorage.getItem('vuetify:dynamic-reload')) {
      console.error('Dynamic import error, reloading page did not fix it', err)
    } else {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  // const role = localStorage.getItem('role') // contoh: 'admin' atau 'user'
  const user = JSON.parse(localStorage.getItem('user') || null)
  const role = user?.role
  console.log('Role', role)
  // Jika butuh login tapi belum login
  if (to.meta.requiresAuth && !token) {
    return next({ path: '/' })
  }

  // Jika route butuh role khusus (misalnya admin)
  if (to.meta.role && to.meta.role !== role) {
    // alert('Anda tidak memiliki akses ke halaman ini.')
    return next({ path: '/dashboard' }) // arahkan ke halaman umum
  }

  next()
})

export default router

<script setup lang="ts">
  import {
    Blend,
    NotepadText,
    UserPen,
    Calculator,
    LayoutDashboard,
    Activity,
    Trophy,
    CircleUserRound,
    Sheet,
  } from 'lucide-vue-next'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'

  // ambil user dari localStorage
const user = JSON.parse(localStorage.getItem('user') || '{}')
const role = user.role || 'guest' // default ke 'guest' jika tidak ada user atau role
console.log('User:', user) // Debug: cek role user

  const dashboard = {
    title: 'Dashboard',
    value: '/dashboard',
    icon: LayoutDashboard,
  }

  const menuItems = [
    {
      title: 'Data Kriteria',
      value: '/criteria',
      icon: Calculator,
    },
    {
      title: 'Data Alternatif',
      value: '/alternative',
      icon: UserPen,
    },
    {
      title: 'Data Penilaian',
      value: '/scoringdata',
      icon: Activity,
    },
    {
      title: 'Data Matriks ',
      value: '/matriksdata',
      icon: Sheet,
    },
    {
      title: 'TOPSIS ',
      value: '/topsisscore',
      icon: NotepadText,
    },
    {
      title: 'Log Data Ranking ',
      value: '/ranking',
      icon: Trophy,
    },
  ]
  const userMenuItems = [
    {
      title: 'Data User',
      value: '/userdata',
      icon: CircleUserRound,
    },
    {
      title: 'Profil Admin',
      value: '/profile',
      icon: CircleUserRound,
    },
  ]

  const activeMenu = ref('home')
  const router = useRouter()

  function selectMenu(value: any) {
    activeMenu.value = value
    router.push(value)
  }
</script>

<template>
  <v-navigation-drawer
    class="!bg-cyan-700 sidebar"
    :elevation="5"
    expand-on-hover
    permanent
    rail
    rail-width="80"
  >
    <v-list>
      <v-list-item>
        <Blend class="top-icon-sidebar" :size="50" />
      </v-list-item>

      <v-divider class="sidebar-divider ma-1" :thickness="2" />

      <!-- Dashboard -->
      <v-list-item
        class="pl-7 py-5"
        @click="selectMenu(dashboard.value)"
        :prepend-icon="dashboard.icon"
      >
        {{ dashboard.title }}
      </v-list-item>

      <!-- Menu umum -->
      <v-list>
        <v-divider class="sidebar-divider ma-1" :thickness="2" />
        <v-list-item
          v-for="item in menuItems"
          :key="item.value"
          class="pl-7 sidebar-icon"
          :prepend-icon="item.icon"
          :title="item.title"
          @click="selectMenu(item.value)"
        />
      </v-list>

      <!-- Menu khusus admin -->
      <v-list v-if="role === 'admin'">
        <v-divider class="sidebar-divider ma-1" :thickness="2" />
        <v-list-item
          v-for="item in userMenuItems"
          :key="item.value"
          class="pl-7 sidebar-icon"
          :prepend-icon="item.icon"
          :title="item.title"
          @click="selectMenu(item.value)"
        />
      </v-list>
    </v-list>
  </v-navigation-drawer>
</template>

<style lang="css" scoped>
  .v-divider.sidebar-divider {
    background-color: red;
    color: white;
  }
  .v-list-item.sidebar-icon--active {
    color: red;
  }

  .v-navigation-drawer.sidebar {
    color: white;
  }
  .criteria {
    text-overflow: unset;
    overflow: visible;
  }
  .top-icon-sidebar {
    height: 63px;
    display: flex;
    justify-content: center;
    margin: 0 auto;
    align-items: center;
    color: ghostwhite;
  }

  .v-navigation-drawer--expanded .sidebar-divider {
    width: 80%;
  }
  .sidebar-divider {
    margin: 0 auto;
  }
</style>

<script setup lang="ts">
  import { UserPen, SquarePlus, LayoutDashboard, Activity } from 'lucide-vue-next'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  // import Logo from '../assets/logo.png'

  const menuItems = [
    {
      title: 'Dashboard',
      value: '/dashboard',
      icon: LayoutDashboard,
    },
    {
      title: 'Calculator',
      value: '/calculator',
      icon: SquarePlus,
    },
    {
      title: 'Team Management',
      value: '/teammanagement',
      icon: UserPen,
    },
    {
      title: 'Playground',
      value: '/playground',
      icon: Activity,
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
      <v-list-item class="d-flex justify-space-around">
        <v-img :height="50" :width="50" />
      </v-list-item>
      <v-list>
        <v-divider class="sidebar-divider" :length="100" :thickness="5" />
        <v-list-item
          v-for="item in menuItems"
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
    color: green;
  }
  .v-list-item.sidebar-icon--active {
    color: red;
  }

  .v-navigation-drawer.sidebar {
    color: white;
  }
</style>

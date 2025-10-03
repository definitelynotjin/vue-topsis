<script lang="ts" setup>
  import { useRoute } from 'vue-router'
  import { Toaster } from 'vue-sonner'
  import 'vue-sonner/style.css'

  const route = useRoute()
</script>

<template>
  <v-app>
    <Toaster theme="light" rich-colors />
    <div v-if="route.path === '/'" class="h-full">
      <router-view />
    </div>

    <div v-else class="full-height-comp">
      <Toaster theme="light" rich-colors />
      <main>
        <VueSidebar />
        <NavBar />
        <!-- <BreadCrumbs class="overflow-auto" /> -->
        <router-view />
      </main>
    </div>
  </v-app>
</template>

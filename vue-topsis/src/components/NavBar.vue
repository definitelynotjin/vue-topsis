<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router'
  import { LogOutIcon } from 'lucide-vue-next'

  const router = useRouter()
  const route = useRoute()

  function handleLogout() {
    localStorage.removeItem('isLoggedIn')
    router.push('/')
  }

  const dynamicTitle = computed(() => {
    if (!route.name) return 'whop'
    return String(route.name)
      .replace(/[-/]/g, ' ')
      .replace(/\b\w /g, (l) => l.toUpperCase())
  })
</script>

<template>
  <v-app-bar app height="80" class="!bg-cyan-800">
    <v-app-title-bar class="pl-10 text-h4 !font-semibold !title-bar"
      >{{ dynamicTitle }}
    </v-app-title-bar>
    <div class="d-flex align-items-center pa-4" />
    <v-spacer />
    <v-btn
      class="button-logout !bg-red-500 mr-20"
      variant="flat"
      :width="100"
      :append-icon="LogOutIcon"
      @click="handleLogout"
    />
  </v-app-bar>
</template>

<style scoped lang="css">
  .title-bar {
    background-color: green;
  }
  .button-logout {
    margin-right: 10rem;

    justify-items: end;
  }
</style>

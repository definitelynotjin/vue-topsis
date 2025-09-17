<script lang="ts" setup>
  import { useRoute } from 'vue-router'

  const route = useRoute()
</script>

<template>
  <v-app>
    <div v-if="route.path === '/'" class="h-full">
      <router-view />
    </div>

    <div v-else class="full-height-comp">
      <main>
        <router-view />
      </main>
    </div>
  </v-app>
</template>

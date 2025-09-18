<script setup lang="ts">
  import { ref } from 'vue'

  const performance = ref([100, 200, 330, 460, 500, 640, 700, 800, 900, 1000])
</script>

<template>
  <v-sparkline
    :model-value="performance"
    class="text-white"
    color="red-darken-4"
    height="60"
    padding="12"
    smooth
  >
    <template v-slot="item" class="text-white"> ${{ item.performance }} </template>
  </v-sparkline>
</template>

<style scoped lang="css"></style>

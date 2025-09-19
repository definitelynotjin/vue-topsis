<script setup lang="ts">
  import { ref } from 'vue'

  const performance = ref([100, 110, 330, 460, 540, 330, 700, 900, 1000])
</script>

<template>
  <v-sparkline :model-value="performance" class="text-white" color="red-darken-4" smooth>
    <template v-slot="item" class="text-white"> ${{ item.performance }} </template>
  </v-sparkline>
</template>

<style scoped lang="css"></style>

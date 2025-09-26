<script setup lang="ts">
  import { ref } from 'vue'

  const performance = ref([100, 110, 330, 460, 540, 330, 700, 900, 1000])
</script>

<template>
  <v-sparkline
    padding="5"
    :model-value="performance"
    class="sparkline-chart"
    line-width="1"
    stroke-linecap="round"
    smooth
  >
    <template v-slot:label="item" class="chart-label font-extralight"> {{ item.value }} </template>
  </v-sparkline>
</template>

<style scoped lang="css">
  .sparkline-chart {
    font-size: 5px;
  }
  .chart-label {
    font-size: 5px;
    color: white;
  }
</style>

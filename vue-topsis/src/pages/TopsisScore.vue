<script setup lang="ts">
  import { ref } from 'vue'
  import { useCriteriaStore } from '@/stores/criteriaStore'
  import { useProjectStore } from '@/stores/projectStore'
  import { useScoreStore } from '@/stores/scoreStore'

  const criteriaStore = useCriteriaStore()
  const projectStore = useProjectStore()
  const scoreStore = useScoreStore()
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="d-flex bg-cyan-700 score-top-table-text"></div>
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }

  .score-container {
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    background-color: steelblue;
  }

  .score-top-table-text {
    font-weight: bold;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
    height: 100px;
    justify-content: space-between;
  }
  .score-add-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }

  .card-edit-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }
</style>

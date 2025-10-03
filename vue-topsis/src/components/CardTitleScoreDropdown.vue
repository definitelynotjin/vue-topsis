<script setup lang="ts">
  import { useProjectStore } from '../stores/projectStore'
  import { useCriteriaStore } from '../stores/criteriaStore'

  const projectStore = useProjectStore()
  const criteriaStore = useCriteriaStore()
</script>

<template>
  <v-select
    class="card-title"
    v-model="projectStore.selectedProjectId"
    :items="projectStore.projects"
    variant="outlined"
    item-title="name"
    item-value="id"
    label="Pilih Projek"
    :list-props="{ bgColor: 'cyan-darken-2' }"
    item-color="white"
  >
  </v-select>

  <v-select
    class="second-card-title"
    v-model="criteriaStore.selectedCriteriaId"
    :disabled="!projectStore.selectedProjectId"
    :items="criteriaStore.criteria"
    variant="outlined"
    item-title="name"
    :list-props="{ bgColor: 'cyan-darken-2' }"
    item-value="id"
    label="Pilih Kriteria"
  >
  </v-select>
</template>

<style scoped lang="css">
  .card-title {
    margin: 15px;
    max-width: 250px;
    height: 30px;
  }

  .second-card-title {
    margin: 15px;
    max-width: 250px;
    height: 30px;
  }
</style>

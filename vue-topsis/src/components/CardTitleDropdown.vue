<script setup lang="ts">
  import { onMounted } from 'vue'
  import { useProjectStore } from '../stores/projectStore.ts'

  const projectStore = useProjectStore()

  onMounted(async () => {
    projectStore.loadAllProjects()
    console.log('thisis the projectsore, ', projectStore.projects)
  })
</script>

<template>
  <v-select
    class="card-title"
    v-model="projectStore.selectedProjectId"
    :items="projectStore.projects"
    variant="outlined"
    item-title="name"
    item-value="id"
    label="Select Project"
    :list-props="{ bgColor: 'cyan-darken-1' }"
    item-color="white"
  >
  </v-select>
</template>

<style scoped lang="css">
  .card-title {
    margin: 14px;
    max-width: 250px;
    height: 30px;
  }
</style>

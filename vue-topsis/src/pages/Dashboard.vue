<script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { ChevronDown } from 'lucide-vue-next'
  import { fetchProjectData } from '../services/api.ts'
  import type { Project } from '../types/type.ts'

  const isDropdownVisible = ref(false)
  const myProject = ref<Project[]>([])
  const dropdowns = ref<Record<number, boolean>>({})

  const toggleDropdownSelect = () => {
    isDropdownVisible.value = !isDropdownVisible.value
  }
  onMounted(async () => {
    myProject.value = await fetchProjectData()
    myProject.value.forEach((project) => {
      dropdowns.value[project.id] = false
    })
  })
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="card-container bg-cyan-700 justify-around">
        <v-card hover class="project-card flex-1" v-for="project in myProject" :key="project.id">
          {{ project.name }}
          <v-row>
            <v-card-text class="project-card-text">
              {{ project.description }}
            </v-card-text>
            <v-card-actions class="action-buttons">
              <v-btn color="white" :icon="ChevronDown" @click="toggleDropdownSelect" />
            </v-card-actions>
          </v-row>
        </v-card>
        <DashboardDropdown />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }
  .card-container {
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    overflow-y: auto;
  }
  .project-card {
    border-radius: 10px;
    height: 10vh;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 15px;
    margin: 10px;
    background-color: steelblue;
  }

  .project-card-text {
    margin: 10px;
    color: floralwhite;
    font-size: 17px;
  }

  .action-buttons {
    justify-items: auto;
    top: 20px;
  }
</style>

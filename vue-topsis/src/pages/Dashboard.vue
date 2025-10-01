<script setup lang="ts">
  import { onMounted, ref, computed } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { ChevronDown, Plus } from 'lucide-vue-next'
  import { fetchProjectData } from '../services/api.ts'

  const projectStore = useProjectStore()
  const searchFilter = ref('')

  const dropdowns = ref<Record<number, boolean>>({})
  const showDialog = ref(false)
  const activeProject = ref(null)

  function openDropdown(project) {
    activeProject.value = project
  }
  function closeDropdown() {
    activeProject.value = null
  }

  const handleSearch = (search) => {
    searchFilter.value = search
  }

  const filteredProject = computed(() => {
    const term = (searchFilter.value ?? '').toLowerCase()
    return projectStore.projects.filter((item) => {
      return (
        item.name?.toLowerCase().includes(term) || item.description?.toLowerCase().includes(term)
      )
    })
  })

  onMounted(async () => {
    projectStore.projects = await fetchProjectData()
    console.log('this is the projecstore data in dasboard', projectStore.projects)
    projectStore.projects.forEach((project) => {
      dropdowns.value[project.id] = false
    })
  })
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="card-container bg-cyan-700">
        <div class="d-flex project-top-card justify-around">
          <SearchBar @search="handleSearch" />
          <v-tooltip text="Add new Project">
            <template v-slot:activator="{ props }">
              <v-btn
                variant="flat"
                v-bind="props"
                @click="showDialog = true"
                :width="100"
                class="!bg-cyan-800 my-2 add-project-button"
              >
                <Plus :size="15" />
              </v-btn>
            </template>
          </v-tooltip>
        </div>
        <div>
          <v-card
            hover
            class="project-card flex-1"
            v-for="project in filteredProject"
            :key="project.id"
          >
            {{ project.name }}
            <v-row>
              <v-card-text class="project-card-text">
                {{ project.description }}
              </v-card-text>
              <v-card-actions class="action-buttons">
                <v-btn
                  color="white"
                  :icon="ChevronDown"
                  @click="
                    activeProject?.id === project.id ? closeDropdown() : openDropdown(project)
                  "
                  @close="closeDropdown"
                />
              </v-card-actions>
            </v-row>
            <DashboardDropdown
              v-if="activeProject?.id === project.id"
              :project="activeProject"
              @close="closeDropdown"
            />
          </v-card>
        </div>
        <v-card
          hover
          class="project-card flex-1"
          v-for="project in filteredProject"
          :key="project.id"
        >
          {{ project.name }}
          <v-row>
            <v-card-text class="project-card-text">
              {{ project.description }}
            </v-card-text>
            <v-card-actions class="action-buttons">
              <v-btn
                color="white"
                :icon="ChevronDown"
                @click="activeProject?.id === project.id ? closeDropdown() : openDropdown(project)"
                @close="closeDropdown"
              />
            </v-card-actions>
          </v-row>

          <DashboardDropdown
            v-if="activeProject?.id === project.id"
            :project="activeProject"
            @close="closeDropdown"
          />
        </v-card>
        <AddProjectDialog v-model="showDialog" @saved="console.log('project saved')" />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }
  .card-container {
    align-items: center;
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
  .add-project-button {
    width: 20px;
    top: 7px;
    height: 50px;
    margin-left: 20px;
  }
  .project-top-card {
    margin: 10px;
    margin-bottom: 30px;
    justify-content: center;
    justify-items: center;
  }
</style>

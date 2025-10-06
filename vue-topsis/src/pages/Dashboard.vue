<script setup lang="ts">
  import { onMounted, ref, computed } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { ChevronDown, Plus, Trash } from 'lucide-vue-next'
  import { fetchProjectData } from '../services/api.ts'


  const projectStore = useProjectStore()
  const searchFilter = ref('')

  const dropdowns = ref<Record<number, boolean>>({})
  const showDialog = ref(false)
  const activeProject = ref(null)
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)
  const showDeleteDialog = ref(false)

  function openDropdown(project: any) {
    activeProject.value = project
  }
  function closeDropdown() {
    activeProject.value = null
  }
    function requestDelete(item: { id: number; name: string }) {
    pendingDeleteId.value = item.id
    pendingDeleteName.value = item.name
    showDeleteDialog.value = true
  }
  async function delProject(projectId: number) {
    if (confirm('Are you sure you want to delete this project?')) {
      await projectStore.deleteProject(projectId)
      if (activeProject.value && activeProject.value.id === projectId) {
        closeDropdown()
      }
    }
  }

  const handleSearch = (search: any) => {
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

  function getProjectName(projectId: number | null) {
    if (!projectId) return 'idk'
    return projectStore.projects.find((p) => p.id === projectId)?.name || 'idk tho'
  }

    async function confirmDelete() {
      console.log('deleted project with id', pendingDeleteId.value)
    if (pendingDeleteId.value !== null) {
      await projectStore.deleteProject(pendingDeleteId.value)
      if (activeProject.value && activeProject.value.id === pendingDeleteId.value) {
        closeDropdown()
      }
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }

  onMounted(async () => {
    projectStore.projects = await fetchProjectData()
    console.log('this is the projecstore data in dasboard', projectStore.projects)
    projectStore.projects.forEach((project) => {
      dropdowns.value[project.id!] = false
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
              <v-card-actions class="action-buttons">
                <v-btn
                  color="white"
                  :icon="Trash"
                  @click=" showDeleteDialog = true
                  "
                />
              </v-card-actions>
              <DeleteProjectDialog
                v-model="showDeleteDialog"
                :project-name="getProjectName(projectStore.selectedProjectId)"
                :alternative-name="pendingDeleteName"
                @confirm-delete="confirmDelete"
              />
            </v-row>
            <DashboardDropdown
              v-if="activeProject?.id === project.id"
              :project="activeProject"
              @close="closeDropdown"
            />
          </v-card>
        </div>
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

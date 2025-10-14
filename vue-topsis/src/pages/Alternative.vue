<script setup lang="ts">
  import { watch, ref, computed } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useAlternativeStore } from '@/stores/alternativeStore'
  import { toast } from 'vue-sonner'

  const projectStore = useProjectStore()
  const alternativeStore = useAlternativeStore()

  const showAddDialog = ref(false)
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)
  const showImportDialog = ref(false)
  const showDeleteDialog = ref(false)

  const searchfilter = ref('')

  const filteredAlternative = computed(() => {
    const term = (searchfilter.value ?? '').toLowerCase()
    return alternativeStore.alternative.filter((item) => {
      return item.id_alt?.toString().includes(term) || item.name.toLowerCase().includes(term)
    })
  })

  function getProjectName(projectId: number | null) {
    if (!projectId) return 'idk'
    return projectStore.projects.find((p) => p.id === projectId)?.name || 'idk tho'
  }

  function requestDelete(item: { id: number; name: string }) {
    pendingDeleteId.value = item.id
    pendingDeleteName.value = item.name
    showDeleteDialog.value = true
  }

  async function handleAlternativeEdit(
    alternative_id: number,
    updated: {
      name?: string
      id_alt?: string
    },
  ) {
    await alternativeStore.editAlternative(alternative_id, updated)
    await alternativeStore.loadByProject(projectStore.selectedProjectId!)
  }

  async function handleExportSuccess() {
    try {
      await alternativeStore.exportAlternative(projectStore.selectedProjectId)
    } catch (error) {
      console.log('damn eror', error)
    }
  }

  async function handleImportSuccess() {
    if (projectStore.selectedProjectId!) {
      await alternativeStore.loadByProject(projectStore.selectedProjectId)
    }
    toast.success('wow, success')
  }

  async function confirmDelete() {
    if (pendingDeleteId.value !== null) {
      await alternativeStore.deleteAlternative(pendingDeleteId.value)
      await alternativeStore.loadByProject(projectStore.selectedProjectId!)
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }
  const handleSearch = (search: string) => {
    searchfilter.value = search
  }
  const altHeaders = [
    { title: 'No', key: 'no', sortable: false, width: '10%' },
    { title: 'ID Alternatif', key: 'id_alt', width: '30%' },
    { title: 'Nama Alternatif', key: 'name' },
    { title: '', key: 'actions', sortable: false, align: 'end', width: '1%' },
  ]
  watch(
    () => projectStore.selectedProjectId,
    async (newId) => {
      if (newId) {
        await alternativeStore.loadByProject(newId)
      } else {
        alternativeStore.alternative = []
      }
    },
    { immediate: true },
  )
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="alternative-container">
        <div class="d-flex !bg-cyan-700 alternative-top-table-text">
          <CardTitleDropdown />
          <SearchBar @search="handleSearch" />
          <v-btn
            :disabled="!projectStore.selectedProjectId"
            @click="showAddDialog = true"
            v-bind="props"
            hover
            type="submit"
            class="!bg-green-600 card-add-button"
            variant="flat"
          >
            Tambah Alternatif
          </v-btn>

          <v-btn
            type="submit"
            hover
            variant="flat"
            @click=""
            class="card-export-button !bg-cyan-600"
          >
            Export Data
          </v-btn>

          <v-btn
            type="submit"
            hover
            variant="flat"
            @click="showImportDialog = true"
            class="card-add-button !bg-cyan-600"
          >
            Import Data
          </v-btn>
        </div>
        <AddAlternativeDialog
          v-model="showAddDialog"
          :project_id="projectStore.selectedProjectId!"
        />
        <DeleteAlternativeDialog
          v-model="showDeleteDialog"
          :project-name="getProjectName(projectStore.selectedProjectId)"
          :alternative-name="pendingDeleteName"
          @confirm-delete="confirmDelete"
        />
        <AddImportDataAlternativeDialog
          v-model="showImportDialog"
          :project_id="projectStore.selectedProjectId!"
          @imported="handleImportSuccess"
        />
        <AlternativeDataTable
          :items="filteredAlternative"
          :headers="altHeaders"
          @edit-alternative="handleAlternativeEdit"
          @delete-request="requestDelete"
        />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .alternative-container {
    padding: 25px;
    margin-top: 70px;
    background-color: steelblue;
    width: 165vh;
    border-radius: 10px;
  }

  .alternative-top-table-text {
    font-weight: bold;
    background-color: darkslategrey;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
  }

  .card-add-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }

  .card-export-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }
</style>

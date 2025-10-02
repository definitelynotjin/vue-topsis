<script setup lang="ts">
  import { computed, watch, ref } from 'vue'
  import { LibraryBig } from 'lucide-vue-next'
  import { useProjectStore } from '@/stores/projectStore'
  import { useCriteriaStore } from '@/stores/criteriaStore'

  const projectStore = useProjectStore()
  const criteriaStore = useCriteriaStore()

  const searchfilter = ref('')
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)
  const showAddDialog = ref(false)
  const showDeleteDialog = ref(false)

  const critHeaders = [
    { title: 'No', key: 'no', sortable: false, width: '10%' },
    { title: 'Nama Kriteria', key: 'name', width: '30%' },
    { title: 'Tipe', key: 'type' },
    { title: 'Bobot', key: 'weight' },
    { title: '', key: 'actions', sortable: false, align: 'end', width: '1%' },
  ]

  const handleSearch = (search: any) => {
    searchfilter.value = search
  }

  function requestDelete(item: { id: number; name: string }) {
    pendingDeleteId.value = item.id
    pendingDeleteName.value = item.name
    showDeleteDialog.value = true
  }
  async function confirmDelete() {
    if (pendingDeleteId.value !== null) {
      await criteriaStore.deleteCriteria(pendingDeleteId.value)
      await criteriaStore.loadByProject(projectStore.selectedProjectId!)
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }
  async function handleEditCriteria(
    criteriaId: number,
    updated: {
      name?: string
      weight?: number
      type?: string
    },
  ) {
    await criteriaStore.editCriteria(criteriaId, updated)
    await criteriaStore.loadByProject(projectStore.selectedProjectId!)
  }

  const filteredCriteria = computed(() => {
    const term = (searchfilter.value ?? '').toLowerCase()
    return criteriaStore.criteria.filter((item) => {
      return (
        item.id?.toString().includes(term) ||
        item.name?.toLowerCase().includes(term) ||
        item.type?.toLowerCase().includes(term) ||
        item.weight?.toString().includes(term)
      )
    })
  })
  watch(
    () => projectStore.selectedProjectId,
    async (newId) => {
      if (newId) {
        await criteriaStore.loadByProject(newId)
      } else {
        criteriaStore.criteria = []
      }
    },
    { immediate: true },
  )
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 criteria-container">
        <div class="d-flex bg-cyan-700 criteria-top-table-text">
          <CardTitleDropdown title="Daftar Data Kriteria" :icon="LibraryBig" />
          <SearchBar @search="handleSearch" />
          <v-btn
            @click="showAddDialog = true"
            :disabled="!projectStore.selectedProjectId"
            v-bind="props"
            hover
            type="submit"
            variant="flat"
            class="card-add-button !bg-cyan-600"
          >
            Tambah Kriteria
          </v-btn>
        </div>
        <AddCriteriaDialog
          v-model="showAddDialog"
          @saved="console.log('saved')"
          :project-id="projectStore.selectedProjectId"
        />
        <DeleteCriteriaDialog
          v-model="showDeleteDialog"
          :criteria-name="pendingDeleteName"
          @confirm-delete="confirmDelete"
        />
        <CriteriaDataTable
          :list-props="{ bgColor: 'cyan-darken-1' }"
          :items="filteredCriteria"
          @edit-criteria="handleEditCriteria!"
          :headers="critHeaders"
          @delete-request="requestDelete"
        />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }

  .criteria-container {
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    background-color: steelblue;
  }

  .criteria-top-table-text {
    font-weight: bold;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
    justify-content: space-between;
  }
  .card-add-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }
</style>

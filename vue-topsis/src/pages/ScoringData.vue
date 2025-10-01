<script setup lang="ts">
  import { ref } from 'vue'
  import { useCriteriaStore } from '@/stores/criteriaStore'
  import { useProjectStore } from '@/stores/projectStore'
  import { useScoreStore } from '@/stores/scoreStore'

  const criteriaStore = useCriteriaStore()
  const projectStore = useProjectStore()
  const scoreStore = useScoreStore()

  const searchFilter = ref('')
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)
  const showAddDialog = ref(false)
  const showDeleteDialog = ref(false)

  const handleSearch = (search) => {
    searchFilter.value = search
  }
  const scoreHeaders = [
    { title: 'No', key: 'no', sortable: false },
    {
      title: 'ID Alternatif',
      key: 'alt_id',
    },

    {
      title: 'Nama Alternatif',
      key: 'name',
    },

    {
      title: 'Nilai',
      key: 'value',
    },

    { title: '', key: 'actions', sortable: false, align: 'end', width: '1%' },
  ]

  const filteredScore = computed(() => {
    const term = (searchFilter.value ?? '').toLowerCase()
    return scoreStore.score.filter((item) => {
      return (
        item.id?.toString().includes(term) ||
        item.alt_id?.toString().includes(term) ||
        item.value?.toString().includes(term)
      )
    })
  })

  function requestDelete(item: { id: number; name: string }) {
    pendingDeleteId.value = item.id
    pendingDeleteName.value = item.name
    showDeleteDialog.value = true
  }

  async function confirmDelete() {
    if (pendingDeleteId.value !== null) {
      await scoreStore.deleteScoreValue(pendingDeleteId.value)
      await scoreStore.loadByCriteria(projectStore.selectedProjectId!, pendingDeleteId.value)
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }

  watch(
    () => projectStore.selectedProjectId,
    async (newProjectId) => {
      if (newProjectId) {
        await criteriaStore.loadByProject(newProjectId)
      } else {
        criteriaStore.criteria = []
      }
    },
    { immediate: true },
  )

  watch(
    [() => projectStore.selectedProjectId, () => criteriaStore.selectedCriteriaId],
    async ([newProjectId, newCriteriaId]) => {
      if (newProjectId && newCriteriaId) {
        await scoreStore.loadByCriteria(newProjectId, newCriteriaId)
      } else {
        scoreStore.score = []
      }
    },
    { immediate: true },
  )
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="d-flex bg-cyan-700 score-top-table-text">
          <CardTitleScoreDropdown />
          <SearchBar @search="handleSearch" />
          <v-btn
            @click="showAddDialog = true"
            v-bind="props"
            hover
            variant="flat"
            type="submit"
            class="card-edit-button !bg-cyan-600"
          >
            Edit Value
          </v-btn>
        </div>
        <EditScoreValueDialog v-model="showDeleteDialog" @confirm-delete="confirmDelete" />
        <ScoreDataTable
          :items="filteredScore"
          :headers="scoreHeaders"
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

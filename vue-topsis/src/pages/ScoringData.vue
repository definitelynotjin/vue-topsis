<script setup lang="ts">
  import { ref } from 'vue'
  import { storeToRefs } from 'pinia'
  import { useCriteriaStore } from '@/stores/criteriaStore'
  import { useScoreStore } from '@/stores/scoreStore'
  import { useProjectStore } from '@/stores/projectStore'

  const criteriaStore = useCriteriaStore()
  const projectStore = useProjectStore()
  const scoreStore = useScoreStore()

  const { selectedProjectId } = storeToRefs(projectStore)
  const { selectedCriteriaId, criteria } = storeToRefs(criteriaStore)
  const { score } = storeToRefs(scoreStore)

  const searchFilter = ref('')
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)
  const showAddDialog = ref(false)
  const showDeleteDialog = ref(false)

  const handleSearch = (search: any) => {
    searchFilter.value = search
  }

  const scoreHeaders = [
    { title: 'No', key: 'no', sortable: false, width: '10%' },
    {
      title: 'ID ',
      key: 'alt_id',
    },

    {
      title: 'ID Alternatif',
      key: 'id_alt',
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
        // item.id_alt?.toString().includes(term) ||
        item.value?.toString().includes(term)
      )
    })
  })

  async function handleEditScoreValue(
    scoreId: number | null,
    updated: { value: number; alternative_id?: number },
  ) {
    console.log('🔍 Editing score value:', { scoreId, updated })
    try {
      if (!scoreId) {
        await scoreStore.addScoreValue({
          value: updated.value,
          alternative_id: updated.alternative_id,
          criteria_id: selectedCriteriaId.value!,
        })
      } else {
        await scoreStore.editScoreValue(scoreId, { value: updated.value })
      }
      await scoreStore.loadByCriteria(selectedProjectId.value!, selectedCriteriaId.value!)
    } catch (error) {
      console.error('damn it error', error)
      throw error
    }
  }

  function requestDelete(item: { score_id: number; name: string }) {
    pendingDeleteId.value = item.score_id
    showDeleteDialog.value = true
  }

  async function confirmDelete() {
    if (pendingDeleteId.value !== null) {
      await scoreStore.deleteScoreValue(pendingDeleteId.value)
      await scoreStore.loadByCriteria(
        projectStore.selectedProjectId!,
        criteriaStore.selectedCriteriaId!,
      )
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }

  watch(
    () => selectedProjectId.value,
    async (newProjectId) => {
      try {
        if (newProjectId) {
          await criteriaStore.loadByProject(newProjectId)
        } else {
          criteria.value = []
        }
      } catch (error) {
        console.error('whoa, error', error)
      }
    },
    { immediate: true },
  )

  watch(
    [() => selectedProjectId.value, () => selectedCriteriaId.value],
    async ([newProjectId, newCriteriaId]) => {
      try {
        if (newProjectId && newCriteriaId) {
          await scoreStore.loadByCriteria(newProjectId, newCriteriaId)
        } else {
          score.value = []
        }
      } catch (error) {
        console.error('whao , another error', error)
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
            readonly
            variant="flat"
            type="submit"
            class="card-edit-button !bg-cyan-600"
          >
          </v-btn>
        </div>
        <DeleteScoreDialog
          :score-id="pendingDeleteId"
          :score-name="pendingDeleteName"
          v-model="showDeleteDialog"
          @confirm-delete="confirmDelete"
        />
        <ScoreDataTable
          :items="filteredScore"
          @edit-value="handleEditScoreValue"
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

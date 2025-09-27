<script setup lang="ts">
  import { ref } from 'vue'
  import { useCriteriaStore } from '@/stores/criteriaStore'
  import { useProjectStore } from '@/stores/projectStore'
  import { useScoreStore } from '@/stores/scoreStore'

  const criteriaStore = useCriteriaStore()
  const projectStore = useProjectStore()
  const scoreStore = useScoreStore()

  const searchFilter = ref('')
  const showDialog = ref(false)

  const handleSearch = (search) => {
    searchFilter.value = search
  }
  const scoreHeaders = [
    {
      title: 'Alternative ID',
      key: 'alt_id',
    },

    {
      title: 'Alternative Name',
      key: 'name',
    },

    {
      title: 'Value',
      key: 'value',
    },

    {
      title: 'Actions',
      key: 'actions',
    },
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

  watch(
    () => projectStore.selectedProjectId,
    async (newProjectId) => {
      if (newProjectId) {
        await criteriaStore.loadByProject(newProjectId)
        criteriaStore.selectedCriteriaId = null
      } else {
        criteriaStore.criteria = []
        criteriaStore.selectedCriteriaId = null
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
            @click="showDialog = true"
            v-bind="props"
            hover
            variant="flat"
            type="submit"
            class="card-edit-button !bg-cyan-600"
          >
            Edit Value
          </v-btn>
        </div>
        <EditScoreValueDialog v-model="showDialog" />
        <DataTable :items="filteredScore" :headers="scoreHeaders" />
        <ActionButtons />
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

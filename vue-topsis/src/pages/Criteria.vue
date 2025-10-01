<script setup lang="ts">
  import { computed, watch, ref } from 'vue'
  import { LibraryBig } from 'lucide-vue-next'
  import { useProjectStore } from '@/stores/projectStore'
  import { useCriteriaStore } from '@/stores/criteriaStore'

  const projectStore = useProjectStore()
  const criteriaStore = useCriteriaStore()

  const searchfilter = ref('')
  const showDialog = ref(false)

  const critHeaders = [
    { title: 'No', key: 'no', sortable: false },
    { title: 'Criteria Name', key: 'name' },
    { title: 'Type', key: 'type' },
    { title: 'Weight', key: 'weight' },
  ]

  const handleSearch = (search) => {
    searchfilter.value = search
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
            @click="showDialog = true"
            :disabled="!projectStore.selectedProjectId"
            v-bind="props"
            hover
            type="submit"
            variant="flat"
            class="card-add-button !bg-cyan-600"
          >
            Add Criteria
          </v-btn>
        </div>
        <AddCriteriaDialog
          v-model="showDialog"
          @saved="console.log('saved')"
          :project-id="projectStore.selectedProjectId"
        />
        <CriteriaDataTable
          :list-props="{ bgColor: 'cyan-darken-1' }"
          :items="filteredCriteria"
          :headers="critHeaders"
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

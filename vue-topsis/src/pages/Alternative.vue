<script setup lang="ts">
  import { watch, ref, computed } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useAlternativeStore } from '@/stores/alternativeStore'

  const projectStore = useProjectStore()
  const alternativeStore = useAlternativeStore()

  const showDialog = ref(false)

  const searchfilter = ref('')

  const filteredAlternative = computed(() => {
    const term = (searchfilter.value ?? '').toLowerCase()
    return alternativeStore.alternative.filter((item) => {
      return (
        item.id?.toString().includes(term) ||
        item.id_alt?.toString().includes(term) ||
        item.name.toLowerCase().includes(term)
      )
    })
  })

  const handleSearch = (search: string) => {
    searchfilter.value = search
  }
  const altHeaders = [
    { title: 'Alternative ID', key: 'id_alt' },
    { title: 'Alternative Name', key: 'name' },
    { title: 'Actions', key: 'actions', sortable: false },
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
            @click="showDialog = true"
            v-bind="props"
            hover
            type="submit"
            class="!bg-cyan-600 card-add-button"
            variant="flat"
          >
            Add Alternative
          </v-btn>
        </div>
        <AddAlternativeDialog v-model="showDialog" :project_id="projectStore.selectedProjectId" />
        <DataTable :items="filteredAlternative" :headers="altHeaders" />
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
    background-color: burlywood;
    text-transform: initial;
  }
</style>

<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useProjectStore } from '@/stores/projectStore'
  import { fetchRankingData } from '@/services/api'
  // import CardTitleDropdown from '@/components/CardTitleScoreDropdown.vue'
  // import TopsisDataTable from '@/components/TopsisDataTable.vue'

  const projectStore = useProjectStore()
  const scores = ref<{ alternative: string; score: number }[]>([])
  const topsisResults = ref({
    scores: [],
    skipped: 0,
    total: 0,
  })
  const loading = ref(false)

  onMounted(() => {
    projectStore.loadAllProjects()
  })

  const topsisHeaders = [
    {
      title: 'No',
      key: 'no',
      sortable: false,
      width: '10%',
    },

    {
      title: 'Nama Alternatif',
      key: 'name',
    },

    {
      title: 'Score TOPSIS',
      key: 'score',
    },
    {
      title: 'Ranking',
      key: 'rank',
    },
  ]

  watch(
    () => projectStore.selectedProjectId,
    async (newProjectId) => {
      if (newProjectId) {
        const res = await fetchRankingData(newProjectId)
        scores.value = res.data
        topsisResults.value = {
          skipped: res.skipped,
          total: res.total,
        }
      } else {
        scores.value = []
        topsisResults.value = {
          skipped: 0,
          total: 0,
        }
      }
    },
    { immediate: true },
  )

  const searchFilter = ref('')
  const search = ref('')
  const handleSearch = (search: string) => {
    searchFilter.value = search
  }
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="d-flex bg-cyan-700 score-top-table-text py-2">
          <CardTitleDropdown />
          <SearchBar @search="handleSearch" />
          <v-btn
            v-bind="props"
            hover
            readonly
            variant="flat"
            type="submit"
            class="card-edit-button !bg-cyan-600"
          >
          </v-btn>
        </div>

        <TopsisDataTable
          :items="scores"
          :skipped="topsisResults.skipped"
          :total="topsisResults.total"
          :headers="topsisHeaders"
        />
        <template v-slot:bottom="slotProps">
          <!-- render pagination bawaan -->
          <v-data-table-footer v-bind="slotProps" />

          <!-- tambahin info custom -->
          <div class="pa-4">
            <p>Data dihitung: {{ props.total }}</p>
            <p>Data tidak dihitung: {{ props.skipped }}</p>
          </div>
        </template>
        <div class="d-flex justify-end">
          <v-btn
            v-if="topsisResults.total"
            type="submit"
            hover
            variant="flat"
            class="card-add-button !bg-green-600"
            :disabled="!topsisResults.total"
            @click="saveRankingReport"
          >
            Save Report
          </v-btn>
        </div>
      </v-container>
    </main>
  </v-app>
</template>

<style scoped>
  .score-container {
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    background-color: steelblue;
  }

  .wallpaper {
    background-color: antiquewhite;
  }

  .score-top-table-text {
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

  .card-title {
    margin: 14px;
    /* max-width: 250px; */
    height: 30px;
  }

  .card-edit-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }
</style>

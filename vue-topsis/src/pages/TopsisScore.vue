<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useTopsisStore } from '@/stores/topsisStore'

  const projectStore = useProjectStore()
  const scores = ref<{ alternative: string; score: number }[]>([])
  const topsisResults = ref({
    scores: [],
    skipped: 0,
    total: 0,
  })
  const loading = ref(false)
  const topsisStore = useTopsisStore()

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

  const searchFilter = ref('')
  const search = ref('')
  const handleSearch = (search: string) => {
    searchFilter.value = search
  }

  const hitungTopsis = async () => {
    if (!projectStore.selectedProjectId) return
    try {
      loading.value = true
      const res = await topsisStore.countTopsis(projectStore.selectedProjectId)
      scores.value = res.data
      topsisResults.value = {
        skipped: res.skipped,
        total: res.total,
      }
    } catch (err) {
      console.error('Gagal hitung Topsis:', err)
      alert('Gagal hitung Topsis!')
    } finally {
      loading.value = false
    }
  }

  const saveRankingReport = async () => {
    if (!projectStore.selectedProjectId || scores.value.length === 0) return
    try {
      loading.value = true
      const res = await topsisStore.saveRankingReport(projectStore.selectedProjectId, scores)
    } finally {
      loading.value = false
    }
  }
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="d-flex bg-cyan-700 score-top-table-text">
          <!-- Dropdown project -->
          <CardTitleDropdown />
          <SearchBar @search="handleSearch" />

          <v-btn
            type="submit"
            hover
            variant="flat"
            class="card-add-button !bg-cyan-600"
            :disabled="!projectStore.selectedProjectId || loading"
            @click="hitungTopsis"
          >
            {{ loading ? 'Menghitung...' : 'Hitung Topsis Score' }}
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
            Simpan Perhitungan
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
</style>

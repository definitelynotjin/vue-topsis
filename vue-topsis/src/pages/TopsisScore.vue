<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useProjectStore } from '@/stores/projectStore'
import TopsisDataTable from '@/components/TopsisDataTable.vue'

const projectStore = useProjectStore()
const scores = ref<{ alternative: string; score: number }[]>([])
const topsisResults = ref({
  scores: [],
  skipped: 0,
  total: 0
})
const loading = ref(false)

onMounted(() => {
  projectStore.loadAllProjects()
})

const topsisHeaders = [
    {
      title: 'No',
      key: 'no',
    },

    {
      title: 'Nama',
      key: 'name',
    },

    {
      title: 'Score TOPSIS',
      key: 'score',
    },
    {
      title: 'Ranking',
      key: 'rank',
    }
  ]




const hitungTopsis = async () => {
  if (!projectStore.selectedProjectId) return
  try {
    loading.value = true
    const res = await axios.get(
      `http://127.0.0.1:5000/topsis/${projectStore.selectedProjectId}`
    )
    // tambahkan nomor urut
    scores.value = res.data.data
    // console.log('res data', res.data.data)
    topsisResults.value = {
      skipped: res.data.skipped,
      total: res.data.total
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
    await axios.post(
      `http://127.0.0.1:5000/topsis/${projectStore.selectedProjectId}/save`
  )
    alert('Laporan ranking berhasil disimpan!')
    console.log('Laporan ranking berhasil disimpan!')
  } catch (err) {
    console.error('Gagal simpan laporan ranking:', err)
    alert('Gagal simpan laporan ranking!')
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
          <v-select
            class="card-title"
            v-model="projectStore.selectedProjectId"
            :items="projectStore.projects"
            variant="outlined"
            item-title="name"
            item-value="id"
            label="Select Project"
            :list-props="{ bgColor: 'cyan-darken-1' }"
            item-color="white"
          />

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
        <TopsisDataTable :items="scores" :skipped="topsisResults.skipped" :total="topsisResults.total" :headers="topsisHeaders" />
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

</style>

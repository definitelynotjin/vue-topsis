<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useMatrixStore } from '@/stores/matrixStore'

  const projectStore = useProjectStore()
  const matrixStore = useMatrixStore()
  const matrix = ref<{ alternative: string; score: number }[]>([])
  const activeMatrixType = ref('')

  const loading = ref(false)

  onMounted(() => {
    projectStore.loadAllProjects()
  })

  const searchFilter = ref('')
  const search = ref('')
  const handleSearch = (search: string) => {
    searchFilter.value = search
  }

  const handleMatriksRaw = async () => {
    if (!projectStore.selectedProjectId) return

    try {
      loading.value = true
      const res = await matrixStore.getMatrixRaw(projectStore.selectedProjectId)
      matrix.value = res.data
      activeMatrixType.value = 'raw'
      // console.log('items:', JSON.stringify(res, null, 2))
    } catch (err) {
      console.error('Gagal fetch matriks awal:', err)
      alert('Gagal fetch matriks awal!')
    } finally {
      loading.value = false
    }
  }

  const handleMatriksNormalisasi = async () => {
    if (!projectStore.selectedProjectId) return
    try {
      loading.value = true
      const res = await matrixStore.getMatrixNormalisasi(projectStore.selectedProjectId)
      matrix.value = res.data
      activeMatrixType.value = 'norm'
    } catch (err) {
      console.error('Gagal fetch matriks normalisasi:', err)
      alert('Gagal fetch matriks normalisasi!')
    } finally {
      loading.value = false
    }
  }

  const handleMatriksBerbobot = async () => {
    if (!projectStore.selectedProjectId) return
    try {
      loading.value = true
      const res = await matrixStore.getMatrixWeighted(projectStore.selectedProjectId)
      matrix.value = res.data
      activeMatrixType.value = 'weight'
    } catch (err) {
      console.error('Gagal fetch matriks berbobot:', err)
      alert('Gagal fetch matriks berbobot!')
    } finally {
      loading.value = false
    }
  }

  const handleIdealSolution = async () => {
    if (!projectStore.selectedProjectId) return
    try {
      loading.value = true
      const res = await matrixStore.getIdealSolution(projectStore.selectedProjectId)
      matrix.value = res.data
      activeMatrixType.value = 'ideal'
    } catch (err) {
      console.error('Gagal fetch solusi ideal:', err)
      alert('Gagal fetch solusi ideal!')
    } finally {
      loading.value = false
    }
  }
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="flex flex-wrap justify-items-end items-end bg-cyan-700 score-top-table-text">
          <div class="flex w-full justify-start">
            <!-- Dropdown project -->
            <CardTitleDropdown />
            <SearchBar @search="handleSearch" />
            <v-btn
              type="submit"
              hover
              variant="flat"
              class="card-export-button !bg-cyan-600"
              :disabled="!projectStore.selectedProjectId || loading"
              @click="hitungTopsis"
            >
              {{ loading ? 'Menghitung...' : 'Export Data' }}
            </v-btn>
          </div>
          <div class="d-flex w-full justify-end">
            <v-btn
              type=""
              hover
              variant="flat"
              :class="
                activeMatrixType === 'raw'
                  ? 'activate-tab card-add-button'
                  : '!bg-cyan-600 card-add-button'
              "
              :disabled="!projectStore.selectedProjectId || loading"
              @click="handleMatriksRaw"
            >
              Matriks Awal
            </v-btn>
            <v-btn
              type=""
              hover
              variant="flat"
              :class="
                activeMatrixType === 'norm'
                  ? 'activate-tab card-add-button'
                  : '!bg-cyan-600 card-add-button'
              "
              :disabled="!projectStore.selectedProjectId || loading"
              @click="handleMatriksNormalisasi"
            >
              Matriks Normalisasi
            </v-btn>
            <v-btn
              type=""
              hover
              variant="flat"
              :class="
                activeMatrixType === 'weight'
                  ? 'activate-tab card-add-button'
                  : '!bg-cyan-600 card-add-button'
              "
              :disabled="!projectStore.selectedProjectId || loading"
              @click="handleMatriksBerbobot"
            >
              Matriks Berbobot
            </v-btn>
            <v-btn
              type=""
              hover
              variant="flat"
              :class="
                activeMatrixType === 'ideal'
                  ? 'activate-tab card-add-button'
                  : '!bg-cyan-600 card-add-button'
              "
              :disabled="!projectStore.selectedProjectId || loading"
              @click="handleIdealSolution"
            >
              Solusi Ideal
            </v-btn>
          </div>
        </div>
        <MatrixDataTable :items="matrix" />
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
    /* margin-top: 10px; */
    padding: 10px;
    border-radius: 10px;
    text-transform: initial;
    justify-content: space-between;
  }

  .card-add-button {
    margin-left: 10px;
    margin-right: 15px;
    margin-top: 20px;
    height: 50px;
    padding: 10px;
    border-radius: 10px 10px 0 0;
    text-transform: initial;
  }

  .card-export-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }

  .card-title {
    margin: 14px;
    height: 30px;
  }

  .activate-tab {
    border-radius: 10px 10px 0 0;
    background-color: steelblue;
  }
</style>

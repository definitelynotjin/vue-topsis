import { defineStore } from 'pinia'
import { addRankingData, fetchTopsisScores } from '@/services/api'

export const useTopsisStore = defineStore('topsis', () => {
  const loading = ref(false)
  const scores = ref<any[]>([])
  const topsisResults = ref<{ skipped: number, total: number }>({ skipped: 0, total: 0 })

  async function countTopsis (projectId: number) {
    if (!projectId) {
      return
    }
    try {
      loading.value = true
      const res = await fetchTopsisScores(projectId)
      scores.value = res.data
      topsisResults.value = {
        skipped: res.skipped,
        total: res.total,
      }
      return res
    } catch (error) {
      console.error('cant count', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  // const countTopsis = async projectId => {
  //   if (!projectId) {
  //     return
  //   }
  //   try {
  //     loading.value = true
  //
  //     const res = await fetchTopsisScores(projectId)
  //
  //     // tambahkan nomor urut
  //     scores.value = res.data
  //     topsisResults.value = {
  //       skipped: res.skipped,
  //       total: res.total,
  //     }
  //     return res
  //   } catch (error) {
  //     console.error('Gagal hitung Topsis:', error)
  //     alert('Gagal hitung Topsis!')
  //   } finally {
  //     loading.value = false
  //   }
  // }

  // const saveRankingReport = async (projectId, scores) => {
  //   if (!projectId || scores.value.length === 0) {
  //     return
  //   }
  //   try {
  //     loading.value = true
  //     const res = await addRankingData(projectId)
  //     alert('Berhasil simpan laporan ranking')
  //   } catch (error) {
  //     console.error('Gagal simpan laporan ranking:', error)
  //     alert('Gagal simpan laporan ranking!')
  //   } finally {
  //     loading.value = false
  //   }
  // }

  async function saveRankingReport (projectId: number) {
    if (!projectId) {
      return
    }
    try {
      loading.value = true
      const res = await addRankingData(projectId)
      return res
    } catch (error) {
      console.error('canot save,', error)
      throw error
    }
  }

  return { loading, scores, topsisResults, countTopsis, saveRankingReport }
})

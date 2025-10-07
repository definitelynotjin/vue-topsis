import { fetchTopsisScores, fetchRankingData, addRankingData } from '@/services/api'
import { useProjectStore } from './projectStore.ts'

export const useTopsisStore = defineStore('topsis', () => {
  const topsisScores = ref<any[]>([])
  const loading = ref(false)
  const projectStore = useProjectStore()
  const scores = ref<any[]>([])
//   const projectId = ref<number | null>(null)
  const topsisResults = ref<{ skipped: number; total: number }>({ skipped: 0, total: 0 })


    const countTopsis = async (projectId) => {
    if (!projectId) return
    try {
        loading.value = true

        const res = await fetchTopsisScores(projectId)

        // tambahkan nomor urut
        scores.value = res.data
        topsisResults.value = {
        skipped: res.skipped,
        total: res.total,
        }
        return res
    } catch (err) {
        console.error('Gagal hitung Topsis:', err)
        alert('Gagal hitung Topsis!')
    } finally {
        loading.value = false
    }
    }

    const saveRankingReport = async (projectId, scores) => {
    if (!projectId || scores.value.length === 0) return
    try {
        loading.value = true
        const res = await addRankingData(projectId)
        alert('Berhasil simpan laporan ranking')
    } catch (err) {
        console.error('Gagal simpan laporan ranking:', err)
        alert('Gagal simpan laporan ranking!')
    } finally {
        loading.value = false
    }
    }

    return {loading, scores, topsisResults, countTopsis, saveRankingReport}

})


import { fetchMatriksRaw, fetchMatriksNormalisasi, fetchMatriksWeighted, fetchIdealSolution } from '@/services/api'

export const useMatrixStore = defineStore('matrix', () => {
  const loading = ref(false)

  const getMatrixRaw = async (projectId) => {
    if (!projectId) return
        try {
            loading.value = true
            const res = await fetchMatriksRaw(projectId)
            console.log('res:', JSON.stringify(res, null, 2))
            return res
        } catch (err) {
            console.error('Gagal fetch Ranking Data:', err)
            alert('Gagal fetch Ranking Data!')
        } finally {
            loading.value = false
        }
    }

    const getMatrixNormalisasi = async (projectId) => {
    if (!projectId) return
        try {
            loading.value = true
            const res = await fetchMatriksNormalisasi(projectId)
            return res
        } catch (err) {
            console.error('Gagal fetch Ranking Data:', err)
            alert('Gagal fetch Ranking Data!')
        } finally {
            loading.value = false
        }

    }
    const getMatrixWeighted = async (projectId) => {
    if (!projectId) return 
        try {
            loading.value = true
            const res = await fetchMatriksWeighted(projectId)
            return res
        } catch (err) {
            console.error('Gagal fetch Ranking Data:', err)
            alert('Gagal fetch Ranking Data!')
        } finally {
            loading.value = false
        }
    }

    const getIdealSolution = async (projectId) => {
    if (!projectId) return
        try {
            loading.value = true
            const res = await fetchIdealSolution(projectId)
            return res
        } catch (err) {
            console.error('Gagal fetch Ranking Data:', err)
            alert('Gagal fetch Ranking Data!')
        } finally {
            loading.value = false
        }   
    }

    return {loading, getMatrixRaw, getMatrixNormalisasi, getMatrixWeighted, getIdealSolution}

})


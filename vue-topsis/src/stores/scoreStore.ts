import type { Score } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addScoreData, deleteScoreData, fetchScoreData, fetchScoresByCriteria } from '@/services/api'
import { useProjectStore } from './projectStore.ts'

export const useScoreStore = defineStore('score', () => {
  const score = ref<Score[]>([])
  const projectStore = useProjectStore()
  const selectedScoreId = ref<number | null>(null)

  async function loadByAlternative (alternative_id: number) {
    score.value = await fetchScoreData(alternative_id)
  }

  async function loadByCriteria (projectId: number, criteriaId: number) {
    score.value = await fetchScoresByCriteria(projectId, criteriaId)
  }

  async function deleteScoreValue (id: number) {
    try {
      const res = await deleteScoreData(id)
      if (selectedScoreId.value !== null) {
        await loadByCriteria(projectStore.selectedProjectId!, selectedScoreId.value)
      }
      return res
    } catch (error) {
      console.error('canot deltee score', error)
      throw error
    }
  }

  async function addScoreValue (newScore: any) {
    if (newScore.value) {
      try {
        const res = await addScoreData(newScore)
        await loadByAlternative(newScore.alternative_id)
        return res
      } catch {
        alert('oi, add score error tangina')
      }
    } else {
      alert('Score value cannot be empty')
    }
  }

  return { loadByAlternative, score, addScoreData, loadByCriteria, deleteScoreValue, addScoreValue }
})

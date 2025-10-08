import type { Score } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { toast } from 'vue-sonner'
import { addScoreData, deleteScoreData, editScoreData, fetchScoreData, fetchScoresByCriteria } from '@/services/api'
import { useCriteriaStore } from './criteriaStore.ts'
import { useProjectStore } from './projectStore.ts'

export const useScoreStore = defineStore('score', () => {
  const score = ref<Score[]>([])
  const projectStore = useProjectStore()
  const criteriaStore = useCriteriaStore()

  async function loadByAlternative (alternative_id: number) {
    score.value = await fetchScoreData(alternative_id)
  }

  async function loadByCriteria (projectId: number, criteriaId: number) {
    score.value = await fetchScoresByCriteria(projectId, criteriaId)
  }

  async function addScoreValue (newScore: any) {
    if (newScore.value) {
      try {
        const res = await addScoreData(newScore)
        await loadByAlternative(newScore.alternative_id)
        return res
      } catch {
        toast.error('Cannot add score!')
      }
    } else {
      alert('Score value cannot be empty')
    }
  }

  async function editScoreValue (scoreId: number, updatedValue: {
    value?: number
  }) {
    try {
      console.log('Editing score:', { scoreId, updatedValue })
      const res = await editScoreData(scoreId, updatedValue)
      await loadByCriteria(projectStore.selectedProjectId!, criteriaStore.selectedCriteriaId!)
      return res
    } catch {
      toast.error('Cannot edit score!')
    }
  }

  async function deleteScoreValue (scoreId: number) {
    try {
      const res = await deleteScoreData(scoreId)
      if (projectStore.selectedProjectId && criteriaStore.selectedCriteriaId) {
        await loadByCriteria(projectStore.selectedProjectId!, criteriaStore.selectedCriteriaId)
      }
      return res
    } catch (error) {
      toast.error('Cannot delete score')
      throw error
    }
  }

  return { loadByAlternative, score, addScoreValue, loadByCriteria, deleteScoreValue, editScoreValue }
})

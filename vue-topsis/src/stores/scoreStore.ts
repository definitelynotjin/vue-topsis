import type { Score } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addScoreData, fetchScoreData, fetchScoresByCriteria } from '@/services/api'

export const useScoreStore = defineStore('score', () => {
  const score = ref<Score[]>([])
  async function loadByAlternative (alternative_id: number) {
    score.value = await fetchScoreData(alternative_id)
  }
  async function loadByCriteria (projectId: number, criteriaId: number) {
    score.value = await fetchScoresByCriteria(projectId, criteriaId)
  }

  async function addScoreValue (newScore) {
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

  return { loadByAlternative, score, addScoreData, loadByCriteria }
})

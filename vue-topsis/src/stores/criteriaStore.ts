import type { Criteria } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addCriteriaData, fetchCriteriaData } from '@/services/api.ts'

export const useCriteriaStore = defineStore('criteria', () => {
  const criteria = ref<Criteria []>([])
  async function loadByProject (projectId: number) {
    criteria.value = await fetchCriteriaData (projectId)
  }
  async function addCriteria (newCriteria) {
    if (newCriteria.project_id && newCriteria.name && newCriteria.type && newCriteria.weight) {
      try {
        const res = await addCriteriaData(newCriteria)
        await loadByProject(newCriteria.project_id)
        return res
      } catch {
        alert('failed man, sorry')
      }
    } else {
      alert('dis cannot be empty tho')
    }
  }
  return { loadByProject, criteria, addCriteria }
})

import type { Criteria } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addCriteriaData, deleteCriteriaData, fetchCriteriaData } from '@/services/api.ts'

export const useCriteriaStore = defineStore('criteria', () => {
  const criteria = ref<Criteria []>([])
  const selectedCriteriaId = ref<number | null>(null)

  async function loadByProject (projectId: number) {
    criteria.value = await fetchCriteriaData (projectId)
  }

  async function deleteCriteria (id: number) {
    try {
      const res = await deleteCriteriaData(id)
      if (selectedCriteriaId.value) {
        await loadByProject(selectedCriteriaId.value)
      }
      return res
    } catch (error) {
      console.error('cant delete crit man', error)
      throw error
    }
  }

  async function addCriteria (newCriteria: {
    project_id: number
    name: string
    type: string
    weight: number
  }) {
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

  function setSelectedCriteriaId (id: number) {
    selectedCriteriaId.value = id
  }

  return { deleteCriteria, loadByProject, criteria, addCriteria, selectedCriteriaId, setSelectedCriteriaId }
})

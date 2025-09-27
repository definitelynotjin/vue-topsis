import type { Criteria } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addCriteriaData, fetchCriteriaData } from '@/services/api.ts'

export const useCriteriaStore = defineStore('criteria', () => {
  const criteria = ref<Criteria []>([])
  const selectedCriteriaId = ref<number | null>(null)
  async function loadByProject (projectId: number) {
    criteria.value = await fetchCriteriaData (projectId)
  }
  // function selectedCriteriaId (id: number) {
  //   selectedCriteriaId.value = id
  // }
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
  return { loadByProject, criteria, addCriteria, selectedCriteriaId, setSelectedCriteriaId }
})

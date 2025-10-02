import type { Criteria } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addCriteriaData, deleteCriteriaData, editCriteriaData, fetchCriteriaData } from '@/services/api.ts'

export const useCriteriaStore = defineStore('criteria', () => {
  const criteria = ref<Criteria []>([])
  const selectedCriteriaId = ref<number | null>(null)
  const selectedProjectId = ref<number | null>(null)

  async function loadByProject (projectId: number) {
    criteria.value = await fetchCriteriaData (projectId)
  }

  function setSelectedCriteriaId (id: number) {
    selectedCriteriaId.value = id
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

  async function editCriteria (criteriaId: number, updatedCriteria: {
    name?: string
    weight?: number
    type?: string
  }) {
    try {
      const res = await editCriteriaData(criteriaId, updatedCriteria)
      await loadByProject(selectedProjectId!)
      return res
    } catch {
      alert('welp, cant edit')
    }
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

  return { deleteCriteria, editCriteria, loadByProject, criteria, addCriteria, selectedCriteriaId, setSelectedCriteriaId }
})

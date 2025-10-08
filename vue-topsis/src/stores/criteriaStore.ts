import type { Criteria } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { toast } from 'vue-sonner'
import { addCriteriaData, deleteCriteriaData, editCriteriaData, fetchCriteriaData } from '@/services/api.ts'
import { useProjectStore } from '@/stores/projectStore.ts'

export const useCriteriaStore = defineStore('criteria', () => {
  const criteria = ref<Criteria []>([])
  const projectStore = useProjectStore()

  const selectedProjectId = computed(() => projectStore.selectedProjectId)
  const selectedCriteriaId = ref<number | null>(null)

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
        toast.error('failed man, sorry')
      }
    } else {
      toast.error('dis cannot be empty tho')
    }
  }

  async function editCriteria (criteriaId: number, updatedCriteria: {
    name?: string
    weight?: number
    type?: string
  }) {
    try {
      const res = await editCriteriaData(criteriaId, updatedCriteria)
      await loadByProject(criteriaId)
      return res
    } catch (error) {
      toast.error('welp, cant edit')
      console.error('cant edit crit man', error)
    }
  }

  async function deleteCriteria (id: number) {
    try {
      const res = await deleteCriteriaData(id)
      if (selectedCriteriaId.value !== null) {
        await loadByProject(selectedProjectId.value!)
      }
      return res
    } catch (error) {
      console.error('cant delete crit man', error)
      throw error
    }
  }

  return { deleteCriteria, editCriteria, loadByProject, criteria, addCriteria, selectedCriteriaId, setSelectedCriteriaId }
})

import type { Alternative } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { toast } from 'vue-sonner'
import { addAlternativeData, deleteAlternativeData, editAlternativeData, fetchAlternativeData, importAlternativeData } from '@/services/api.ts'

export const useAlternativeStore = defineStore('alternative', () => {
  const alternative = ref<Alternative []>([])
  const selectedProjectId = ref<number | null>(null)

  async function loadByProject (projectId: number) {
    alternative.value = await fetchAlternativeData (projectId)
  }

  async function addAlternative (newAlternative: {
    project_id: number
    name: string
    id_alt: number
  }) {
    if (newAlternative.project_id && newAlternative.name && newAlternative.id_alt) {
      try {
        const res = await addAlternativeData(newAlternative)
        await loadByProject(newAlternative.project_id)
        return res
      } catch {
        toast.error('Cannot add alternative!')
      }
    } else {
      alert('alternative cannot be empty')
    }
  }
  async function editAlternative (alternative_id: number, updatedAlternative: {
    name?: string
    id_alt?: string
  }) {
    try {
      const res = await editAlternativeData(alternative_id, updatedAlternative)
      await loadByProject(alternative_id)
      return res
    } catch {
      toast.error('Cannot edit alternative!')
    }
  }

  async function deleteAlternative (id: number) {
    try {
      const res = await deleteAlternativeData(id)
      return res
    } catch (error) {
      toast.error('Cannot delete alternative!')
      throw error
    }
  }
  async function importAlternative (projectId: number, file: File) {
    console.log('this shting is triggered by', { projectId, file })
    try {
      const res = await importAlternativeData(projectId, file)
      await loadByProject(projectId)
      return res
    } catch (error) {
      toast.error('Cannot import alterantive!')
      throw error
    }
  }

  return { loadByProject, alternative, addAlternative, deleteAlternative, editAlternative, importAlternative }
})

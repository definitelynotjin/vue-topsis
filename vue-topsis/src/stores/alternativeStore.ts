import type { Alternative } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addAlternativeData, deleteAlternativeData, editAlternativeData, fetchAlternativeData } from '@/services/api.ts'

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
      } catch (error) {
        console.error('big error alternaive', error)
        alert('woah, alternive fucked')
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
      await loadByProject(selectedProjectId)
      return res
    } catch (error) {
      console.error('edit store cant edit eh', error)
    }
  }

  async function deleteAlternative (id: number) {
    try {
      const res = await deleteAlternativeData(id)
      return res
    } catch (error) {
      console.error('sorry man failed delete alt ehehe', error)
      throw error
    }
  }
  return { loadByProject, alternative, addAlternative, deleteAlternative, editAlternative }
})

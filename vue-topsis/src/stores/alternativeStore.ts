import type { Alternative } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addAlternativeData, deleteAlternativeData, fetchAlternativeData } from '@/services/api.ts'

export const useAlternativeStore = defineStore('alternative', () => {
  const alternative = ref<Alternative []>([])
  async function loadByProject (projectId: number) {
    alternative.value = await fetchAlternativeData (projectId)
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
  async function addAlternative (newAlternative) {
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
  return { loadByProject, alternative, addAlternative, deleteAlternative }
})

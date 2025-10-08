import type { Project } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addProjectData, deleteProjectData, fetchProjectData } from '@/services/api.ts'

export const useProjectStore = defineStore('project', () => {
  const projects = ref<Project[]>([])
  const selectedProjectId = ref<number | null>(null)

  async function loadAllProjects () {
    projects.value = await fetchProjectData()
  }

  async function addProject (newProject: { name: string, description: string }) {
    if (newProject.name && newProject.description) {
      try {
        const res = await addProjectData(newProject)
        await loadAllProjects()
        return res
      } catch {
        alert('cannot add project tngina')
      }
    } else {
      alert('Project cannot be empty')
    }
  }

  async function deleteProject (projectId: number) {
    try {
      const res = await deleteProjectData(projectId)
      console.log('statsus delete project store', res)
      await loadAllProjects()
      return res
    } catch (error) {
      console.error('Error : deleteProjectData', error)
      throw error
    }
  }

  function setSelectedProjectId (id: number | null) {
    selectedProjectId.value = id
  }
  return { setSelectedProjectId, loadAllProjects, projects, selectedProjectId, addProject, deleteProject }
})

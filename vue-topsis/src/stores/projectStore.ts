import type { Project } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addProjectData, fetchProjectData } from '@/services/api.ts'

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
        return res
      } catch {
        alert('cannot add project tngina')
      }
    } else {
      alert('Project cannot be empty')
    }
  }

  function setSelectedProjectId (id: number | null) {
    selectedProjectId.value = id
  }
  return { setSelectedProjectId, loadAllProjects, projects, selectedProjectId, addProject }
})

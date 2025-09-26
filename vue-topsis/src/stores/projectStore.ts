import type { Project } from '../types/type.ts'
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchProjectData } from '@/services/api.ts'

export const useProjectStore = defineStore('project', () => {
  const projects = ref<Project[]>([])
  const selectedProjectId = ref<number | null>(null)

  async function loadAllProjects () {
    projects.value = await fetchProjectData()
  }

  function setSelectedProjectId (id: number | null) {
    selectedProjectId.value = id
  }
  return { setSelectedProjectId, loadAllProjects, projects, selectedProjectId }
})

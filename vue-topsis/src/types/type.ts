export interface Project {
  name?: string
  id: number
  description: string
}

export interface Criteria {
  id?: number
  name: string
  project_id: number
  type: string
  weight: number
}

export interface Alternative {
  name: string
  project_id: number
  type: string
  weight: number
}

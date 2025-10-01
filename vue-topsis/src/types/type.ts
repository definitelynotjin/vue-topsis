export interface Project {
  name: string
  id?: number
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
  id_alt?: number
  name: string
  project_id: number
  type: string
  weight: number
}
export interface Score {
  alt_id: number
  project_id: number
  criteria: string
  id?: number
  value: number
}

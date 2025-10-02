import axios from 'axios'

// Projects

export async function fetchProjectData () {
  try {
    const response = await axios.get('api/project/')
    return response.data
  } catch {
    return []
  }
}
export async function addProjectData (newProject: { name: string, description: string }) {
  try {
    const response = await axios.post('api/project/', newProject)
    return response.data
  } catch (error) {
    console.error('Error : addProjectData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Criterias

export async function fetchCriteriaData (id: number) {
  try {
    const response = await axios.get(`api/criteria/${id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchCriteriaData', error)
    return []
  }
}

export async function addCriteriaData (newCriteria: {
  project_id: number
  name: string
  weight: number
  type: string
}) {
  try {
    const response = await axios.post(`api/criteria`, newCriteria)
    return response.data
  } catch (error) {
    console.error('Error : addCriteriaData', error)
    throw error
  }
}

export async function editCriteriaData (criteriaId: number, updatedCriteria: {
  name?: string
  weight?: number
  type?: string
}) {
  try {
    const response = await axios.put(`api/criteria/${criteriaId}`, updatedCriteria)
    return response.data
  } catch (error) {
    console.error('Error : editCriteriaData', error)
    throw error
  }
}

export async function deleteCriteriaData (criteriaId: number) {
  try {
    const response = await axios.delete(`api/criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteCriteriaData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Alternatives

export async function fetchAlternativeData (id: number) {
  try {
    const response = await axios.get(`api/alternative/${id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchAlternativeData', error)
    return []
  }
}

export async function addAlternativeData (newAlternative: {
  project_id: number
  name: string
  alternative_id: number
}) {
  try {
    const response = await axios.post(`api/alternative`, newAlternative)
    return response.data
  } catch (error) {
    console.error('Error : addAlternativeData', error)
    throw error
  }
}

export async function editAlternativeData (alternative_id: number, updatedAlternative: {
  name?: string
  id_alt?: string
}) {
  try {
    const response = await axios.put(`api/alternative/${alternative_id}`, updatedAlternative)
    return response.data
  } catch (error) {
    console.error('Error : editAlternativeData', error)
    throw error
  }
}
export async function deleteAlternativeData (alternative_id: number) {
  try {
    const response = await axios.delete(`api/alternative/${alternative_id}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteAlternativeData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Scores

export async function fetchScoreData (alternative_id: number) {
  try {
    const response = await axios.get(`api/score/${alternative_id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchScoreData', error)
    return []
  }
}

export async function fetchScoresByCriteria (projectId: number, criteriaId: number) {
  try {
    const response = await axios.get(`api/score/project/${projectId}/criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchScoresByCriteria', error)
    throw error
  }
}
export async function deleteScoreData (scoreId: number) {
  try {
    const response = await axios.delete(`api/score/${scoreId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteScoreData', error)
    throw error
  }
}
export async function editScoreData (scoreId: number, updatedValue: number) {
  try {
    const response = await axios.put(`api/score/${scoreId}`, updatedValue)
    return response.data
  } catch (error) {
    console.error('Error : editScoreData', error)
    throw error
  }
}

export async function addScoreData (newScore: { value: number, alternative_id: number, criteria_id: number }) {
  try {
    const response = await axios.post(`api/score/`, newScore)
    return response.data
  } catch (error) {
    console.error('Error : addScoreData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Topsis Scores

export async function fetchTopsisScores (projectId: number) {
  try {
    const response = await axios.get(`api/topsis/${projectId}`)
    return response.data
  } catch (error) {
    console.error('error fetchTopsisScores', error)
    throw error
  }
}

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
    console.error('error adding project', error)
    throw error
  }
}

// Criterias

export async function fetchCriteriaData (id: number) {
  try {
    const response = await axios.get(`api/criteria/${id}`)
    console.log('thisis is crtieira data', response.data)
    return response.data
  } catch (error) {
    console.error('error crtieria', error)
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
    console.error('cannto add criteira eh', error)
    throw error
  }
}
export async function deleteCriteriaData (criteriaId: number) {
  try {
    const response = await axios.delete(`api/criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('canot delet criteria', error)
    throw error
  }
}

// Alternatives

export async function fetchAlternativeData (id: number) {
  try {
    const response = await axios.get(`api/alternative/${id}`)
    console.log('thisis is alternaie data', response.data)
    return response.data
  } catch (error) {
    console.error('error latenraive', error)
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
    console.error('cannto add altenraive eh', error)
    throw error
  }
}
export async function deleteAlternativeData (alternative_id: number) {
  try {
    const response = await axios.delete(`api/alternative/${alternative_id}`)
    return response.data
  } catch (error) {
    console.error('cannot delete atelratnive eh', error)
    throw error
  }
}

// Scores

export async function fetchScoreData (alternative_id: number) {
  try {
    const response = await axios.get(`api/score/${alternative_id}`)
    console.log('thisis the score data', response.data)
    return response.data
  } catch (error) {
    console.error('error score', error)
    return []
  }
}

export async function fetchScoresByCriteria (projectId: number, criteriaId: number) {
  try {
    const response = await axios.get(`api/score/project/${projectId}/criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('error fetchScoresByCriteria', error)
    throw error
  }
}
export async function deleteScoreData (scoreId: number) {
  try {
    const response = await axios.delete(`api/score/${scoreId}`)
    return response.data
  } catch (error) {
    console.error('sorry man cannot deltee score', error)
    throw error
  }
}
export async function editScoreData (scoreId: number, newValue: number) {
  try {
    const response = await axios.put(`api/score/${scoreId}`, {
      value: newValue,
    })
    return response
  } catch (error) {
    console.error('error editScoreValue', error)
    throw error
  }
}

export async function addScoreData (newScore: { value: number, alternative_id: number, criteria_id: number }) {
  try {
    const response = await axios.post(`api/score/`, newScore)
    return response.data
  } catch (error) {
    console.error('oi, add score data from api error tangina', error)
    throw error
  }
}
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

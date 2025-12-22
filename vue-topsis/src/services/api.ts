import axios from 'axios'
import api from './axiosInstance'

const token = localStorage.getItem('token')

// Projects

export async function fetchProjectData() {
  try {
    const response = await api.get('project/')
    // console.log('Response from fetchProjectData API:', response)
    return response.data
  } catch (error) {
    console.error('Error : fetchProjectData', error)
    return []
  }
}

export async function addProjectData(newProject: { name: string; description: string }) {
  try {
    const response = await api.post('project/', newProject)
    // token = localStorage.getItem('access_token')
    console.log('Response from addProjectData API:', response)
    return response.data
  } catch (error) {
    console.error('Error : addProjectData', error)
    throw error
  }
}

export async function deleteProjectData(projectId: number) {
  try {
    const response = await api.delete(`project/${projectId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteProjectData', error)
    throw error
  }
}

// Login
export async function login(credentials: { username: string; password: string }) {
  try {
    const response = await api.post('api/login/auth', credentials)
    // console.log('Response from login API:', response)
    return response
  } catch (error) {
    console.error('Error : login', error)
    throw error
  }
}

// Logout
export async function logout() {
  try {
    // const response = await api.post('api/logout')
    localStorage.removeItem('token')
    window.location.href = '/' // Redirect to login page after logout
    // return response.data
  } catch (error) {
    console.error('Error : logout', error)
    throw error
  }
}

export async function fetchUsersData() {
  try {
    const response = await api.get(`/user/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    return response.data
  } catch (error) {
    console.error('Error : getAllUsersData', error)
    throw error
  }
}

export async function fetchUserData(userId: number) {
  try {
    const response = await api.get(`/user/${userId}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchUserData', error)
    throw error
  }
}

export async function registerUserData(newUser: {
  username: string
  password?: string
  id?: number
  role: string
}) {
  try {
    const response = await api.post(`/user/register`, newUser)
    return response.data
  } catch (error) {
    console.error('Error : registerUserData', error)
    throw error
  }
}

export async function editUserData(
  userId: number,
  updatedValue: {
    username?: string
    password?: string
    role?: string
  },
) {
  try {
    const response = await api.put(`/user/${userId}`, updatedValue)
    return response.data
  } catch (error) {
    console.error('Error : editUserData', error)
    throw error
  }
}

export async function deleteUserData(userId: number) {
  try {
    const response = await api.delete(`/user/${userId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteUserData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Criterias

export async function fetchCriteriaData(id: number) {
  try {
    const response = await api.get(`criteria/${id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchCriteriaData', error)
    return []
  }
}

export async function addCriteriaData(newCriteria: {
  project_id: number
  name: string
  weight: number
  type: string
}) {
  try {
    const response = await api.post(`criteria`, newCriteria)
    return response.data
  } catch (error) {
    console.error('Error : addCriteriaData', error)
    throw error
  }
}

export async function editCriteriaData(
  criteriaId: number,
  updatedCriteria: {
    name?: string
    weight?: number
    type?: string
  },
) {
  try {
    const response = await api.put(`criteria/${criteriaId}`, updatedCriteria)
    return response.data
  } catch (error) {
    console.error('Error : editCriteriaData', error)
    throw error
  }
}

export async function deleteCriteriaData(criteriaId: number) {
  try {
    const response = await api.delete(`criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteCriteriaData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Alternatives

export async function fetchAlternativeData(id: number) {
  try {
    const response = await api.get(`alternative/${id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchAlternativeData', error)
    return []
  }
}

export async function addAlternativeData(newAlternative: {
  project_id: number
  name: string
  alternative_id: number
}) {
  try {
    const response = await api.post(`alternative`, newAlternative)
    return response.data
  } catch (error) {
    console.error('Error : addAlternativeData', error)
    throw error
  }
}

export async function editAlternativeData(
  alternative_id: number,
  updatedAlternative: {
    name?: string
    id_alt?: string
  },
) {
  try {
    const response = await api.put(`alternative/${alternative_id}`, updatedAlternative)
    return response.data
  } catch (error) {
    console.error('Error : editAlternativeData', error)
    throw error
  }
}

export async function deleteAlternativeData(alternative_id: number) {
  try {
    const response = await api.delete(`alternative/${alternative_id}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteAlternativeData', error)
    throw error
  }
}

export async function importAlternativeData(projectId: number, file: File) {
  try {
    const formData = new FormData()
    formData.append('file', file)
    console.log('FormData keys:', [...formData.keys()])

    const response = await api.post(`import/import/${projectId}`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    return response.data
  } catch (error) {
    console.error('Error : importAlternativeData', error)
    throw error
  }
}

export async function exportAlternativeData(projectId: number) {
  try {
    const response = await api.get(`export/${projectId}`)
    return response.data
  } catch (error) {
    console.error('Error : exportAlternativeData', error)
  }
}

// -------------------------------------------------------------------//

// Scores

export async function fetchScoreData(alternative_id: number) {
  try {
    const response = await api.get(`score/${alternative_id}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchScoreData', error)
    return []
  }
}

export async function fetchScoresByCriteria(projectId: number, criteriaId: number) {
  try {
    const response = await api.get(`score/project/${projectId}/criteria/${criteriaId}`)
    return response.data
  } catch (error) {
    console.error('Error : fetchScoresByCriteria', error)
    return []
  }
}
export async function deleteScoreData(scoreId: number) {
  try {
    const response = await api.delete(`score/${scoreId}`)
    return response.data
  } catch (error) {
    console.error('Error : deleteScoreData', error)
    throw error
  }
}
export async function editScoreData(
  scoreId: number,
  updatedValue: {
    value: number
  },
) {
  try {
    const response = await api.put(`score/${scoreId}`, updatedValue)
    console.log('Response from editScoreData API:', response)
    return response.data
  } catch (error) {
    console.error('Error : editScoreData', error)
    throw error
  }
}

export async function addScoreData(newScore: {
  value: number
  alternative_id: number
  criteria_id: number
}) {
  try {
    const response = await api.post(`score/`, newScore)
    return response.data
  } catch (error) {
    console.error('Error : addScoreData', error)
    throw error
  }
}

// -------------------------------------------------------------------//

// Matriks Raw
export async function fetchMatriksRaw(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}/matrix-raw`)
    return response.data
  } catch (error) {
    console.error('Error : fetchMatriksRaw', error)
    return []
  }
}

// Matriks Normalisasi
export async function fetchMatriksNormalisasi(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}/matrix-normalized`)
    return response.data
  } catch (error) {
    console.error('Error : fetchMatriksNormalisasi', error)
    return []
  }
}

// Matriks Weighted
export async function fetchMatriksWeighted(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}/matrix-weight`)
    return response.data
  } catch (error) {
    console.error('Error : fetchMatriksWeighted', error)
    return []
  }
}

// Ideal Solution
export async function fetchIdealSolution(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}/ideal-solution`)
    return response.data
  } catch (error) {
    console.error('Error : fetchIdealSolution', error)
    return []
  }
}

// Topsis Scores

export async function fetchTopsisScores(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}`)
    return response.data
  } catch (error) {
    console.error('error fetchTopsisScores', error)
    return []
  }
}

// Ranking
export async function fetchRankingData(projectId: number) {
  try {
    const response = await api.get(`topsis/${projectId}/results`)
    return response.data
  } catch (error) {
    console.error('Error : fetchRankingData', error)
    throw error
  }
}

export async function addRankingData(projectId: number) {
  try {
    const response = await api.post(`topsis/${projectId}/save`)
    return response.data
  } catch (error) {
    console.error('Error : fetchRankingData', error)
    throw error
  }
}

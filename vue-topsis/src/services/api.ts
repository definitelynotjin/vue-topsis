import axios from 'axios'

export async function fetchProjectData () {
  try {
    const response = await axios.get('api/project/')
    return response.data
  } catch {
    return []
  }
}

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
export async function deleteCriteriaData (id: number) {
  try {} catch {}
}

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

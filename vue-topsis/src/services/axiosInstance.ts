import axios from "axios"

// Buat instance baru
// console.log('API Base URL:', import.meta.env.VITE_API_BASE_URL);
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL, // ubah sesuai backend kamu
  headers: {
    "Content-Type": "application/json",
  },
})

// Tambahkan interceptor untuk request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token")
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Tambahkan interceptor untuk response (handle 401)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem("token")
      window.location.href = "/login" // redirect kalau token invalid
    }
    return Promise.reject(error)
  }
)

export default api

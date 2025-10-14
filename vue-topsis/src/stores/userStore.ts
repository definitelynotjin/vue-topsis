import type { User } from '@/types/type'
import { defineStore } from 'pinia'
import { deleteUserData, editUserData, fetchUsersData, registerUserData } from '@/services/api'

export const useUserStore = defineStore('user', () => {
  const users = ref<User[]>([])
  const selectedUserId = ref<number | null>(null)

  function setSelectedUserId (id: number | null) {
    selectedUserId.value = id
  }

  async function loadAllUsers () {
    users.value = await fetchUsersData()
  }

  async function registerUser (newUser: {
    username: string
    password?: string
    role: string
  }) {
    try {
      const response = await registerUserData(newUser)
      await loadAllUsers()
      return response.data
    } catch (error) {
      console.error('canot erigster new user eh', error)
      throw error
    }
  }

  async function editUser (userId: number, updatedUser: {
    username?: string
    password?: string
    role?: string
  }) {
    try {
      const response = await editUserData(userId, updatedUser)
      await loadAllUsers()
      return response.data
    } catch (error) {
      console.error('cant edit user eh what,', error)
      throw error
    }
  }

  async function deleteUser (userId: number) {
    try {
      const response = await deleteUserData(userId)
      await loadAllUsers()
      return response.data
    } catch (error) {
      console.error('canot dlete user eh,', error)
      throw error
    }
  }

  return { loadAllUsers, users, registerUser, deleteUser, editUser, setSelectedUserId }
})

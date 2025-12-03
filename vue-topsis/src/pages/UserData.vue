<script setup lang="ts">
  import { onMounted, ref, computed } from 'vue'
  import { useUserStore } from '@/stores/userStore'
  import { Plus, Trash, Pen } from 'lucide-vue-next'
  import { fetchUsersData } from '@/services/api'
  import { capitalizeFirst } from '../utils/capitalizeFirst.ts'

  const userStore = useUserStore()
  const searchFilter = ref('')

  const showAddDialog = ref(false)
  const showEditDialog = ref(false)
  const showDeleteDialog = ref(false)
  const pendingDeleteId = ref<number | null>(null)
  const pendingDeleteName = ref<string | null>(null)

  const selectedUser = ref<any>(null)

  function requestDelete(item: { id: number; username: string; role: string }) {
    pendingDeleteId.value = item.id ?? null
    pendingDeleteName.value = item.username
    showDeleteDialog.value = true
  }

  async function confirmDelete() {
    if (pendingDeleteId.value !== null) {
      await userStore.deleteUser(pendingDeleteId.value)
      await userStore.loadAllUsers()
    }
    showDeleteDialog.value = false
    pendingDeleteId.value = null
  }

  const handleSearch = (search: any) => {
    searchFilter.value = search
  }

  const filteredUser = computed(() => {
    const term = (searchFilter.value ?? '').toLowerCase()
    return userStore.users.filter((item) => {
      return item.username?.toLowerCase().includes(term) || item.role?.toLowerCase().includes(term)
    })
  })

  onMounted(async () => {
    userStore.users = await fetchUsersData()
  })
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="card-container bg-cyan-700">
        <div class="d-flex user-top-card justify-around">
          <SearchBar @search="handleSearch" />
          <v-tooltip text="Add new User">
            <template v-slot:activator="{ props }">
              <v-btn
                variant="flat"
                v-bind="props"
                @click="showAddDialog = true"
                :width="100"
                class="!bg-cyan-800 my-2 add-user-button"
              >
                <Plus :size="15" />
              </v-btn>
            </template>
          </v-tooltip>
        </div>
        <div>
          <v-card hover class="user-card flex-1" v-for="user in filteredUser" :key="user.id">
            {{ user.username }}
            <v-row>
              <v-card-text class="user-card-text">
                {{ capitalizeFirst(user.role) }}
              </v-card-text>
              <v-card-actions class="action-buttons">
                <v-btn
                  color="white"
                  :icon="Pen"
                  @click="
                    () => {
                      showEditDialog = true
                    }
                  "
                />
                <v-btn color="red" :icon="Trash" @click="requestDelete(user)" />
              </v-card-actions>
              <DeleteUserDialog
                v-model="showDeleteDialog"
                :user-id="pendingDeleteId"
                :user-name="pendingDeleteName"
                @confirm-delete="confirmDelete"
              />
            </v-row>
          </v-card>
        </div>
        <AddUserDialog v-model="showAddDialog" />
        <EditUserDialog
          v-model="showEditDialog"
          :user-id="selectedUser?.id || 0"
          :user-name="selectedUser?.username || ''"
          :user-pass="selectedUser?.password || ''"
          :user-role="selectedUser?.role || ''"
          @saved="userStore.loadAllUsers"
        />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }
  .card-container {
    align-items: center;
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    overflow-y: auto;
  }
  .user-card {
    border-radius: 10px;
    height: 10vh;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 15px;
    margin: 10px;
    background-color: steelblue;
  }

  .user-card-text {
    margin: 10px;
    color: floralwhite;
    font-size: 17px;
  }

  .action-buttons {
    justify-items: auto;
    top: 20px;
  }
  .add-user-button {
    width: 20px;
    top: 7px;
    height: 50px;
    margin-left: 20px;
  }
  .user-top-card {
    margin: 10px;
    margin-bottom: 30px;
    justify-content: center;
    justify-items: center;
  }
</style>

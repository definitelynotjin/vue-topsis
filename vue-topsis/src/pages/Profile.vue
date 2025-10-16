<script setup lang="ts">
  import { User } from 'lucide-vue-next'
  import { useUserStore } from '../stores/userStore'

  const userStore = useUserStore()
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="card-container bg-cyan-700">
        <div class="d-flex profile-top-card justify-around">
          <v-tooltip text="Add new User">
            <template v-slot:activator="{ props }">
              <v-btn
                variant="flat"
                v-bind="props"
                :width="100"
                class="!bg-cyan-800 my-2 add-user-button"
              >
                <Plus :size="15" />
              </v-btn>
            </template>
          </v-tooltip>
        </div>
        <div>
          <v-card hover class="profile-card flex-1" v-for="user in filteredUser" :key="user.id">
            <v-row>
              <v-card-actions class="action-buttons"> </v-card-actions>
            </v-row>
          </v-card>
        </div>
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
  .profile-card {
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
  .profile-top-card {
    margin: 10px;
    margin-bottom: 30px;
    justify-content: center;
    justify-items: center;
  }
</style>

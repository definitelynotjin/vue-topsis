<script setup lang="ts">
  import { Eye, Trash, SquarePen } from 'lucide-vue-next'
  const cardItems = ref([
    {
      text: 'Project 1',
      description: '',
      value: [
        {
          Best: 'Kurniawan',
          Worst: 'Ferdi',
        },
      ],
    },

    {
      text: 'Project 2',
      description: '',
      value: [
        {
          Best: 'Budiawan',
          Worst: 'Setya',
        },
      ],
    },

    {
      text: 'Project 3',
      description: '',
      value: [
        {
          Best: 'Gatot',
          Worst: 'Sera',
        },
      ],
    },

    {
      text: 'Project 4',
      description: '',
      value: [
        {
          Best: 'Asep',
          Worst: 'Eko',
        },
      ],
    },
  ])
</script>

<template>
  <v-app class="wallpaper">
    <main>
      <v-container fluid class="card-container">
        <v-row justify="space-around">
          <v-card hover class="project-card flex-1" v-for="item in cardItems" :key="item">
            {{ item.text }}
            <v-row justify="end">
              <v-card-actions>
                <v-btn color="gray" :icon="Eye" />
                <v-btn color="gray" :icon="SquarePen" />
                <v-btn color="red" :icon="Trash" />
              </v-card-actions>
            </v-row>
          </v-card>
        </v-row>
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: darkslategrey;
  }

  .card-container {
    padding: 25px;
    margin-top: 70px;
    background-color: burlywood;
    width: 165vh;
    border-radius: 10px;
  }
  .project-card {
    height: 30vh;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 15px;
    margin: 10px;
    background-color: darkslategrey;
  }
</style>

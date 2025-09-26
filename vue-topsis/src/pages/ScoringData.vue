<script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { fetchScoreData } from '../services/api.ts'

  const scoreData = ref([])
  const searchFilter = ref('')

  const handleSearch = (search) => {
    searchFilter.value = search
  }
  const showDialog = ref(false)
  const scoreHeaders = [
    {
      title: 'ID',
      key: 'project_id',
    },

    {
      title: 'Nama alternatif',
      key: 'alternative.name',
    },

    {
      title: 'Type',
      key: 'type',
    },

    {
      title: 'Weight',
      key: 'weight',
    },

    {
      title: 'ID',
      key: 'project_id',
    },
  ]

  onMounted(async () => {
    scoreData.value = await fetchScoreData(1)
  })
</script>

<template>
  <v-app class="!bg-cyan-900">
    <main>
      <v-container fluid class="bg-cyan-700 score-container">
        <div class="d-flex bg-cyan-700 score-top-table-text">
          <CardTitleDropdown />
          <SearchBar @search="handleSearch" />
          <v-btn
            @click="showDialog = true"
            v-bind="props"
            hover
            type="submit"
            class="score-add-button !bg-cyan-600"
          >
            Tambahkan Kriteria
          </v-btn>
        </div>
        <AddCriteriaDialog v-model="showDialog" />
        <DataTable :items="scoreData" :headers="scoreHeaders" />
        <ActionButtons />
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: antiquewhite;
  }

  .score-container {
    padding: 25px;
    margin-top: 70px;
    width: 165vh;
    border-radius: 10px;
    background-color: steelblue;
  }

  .score-top-table-text {
    font-weight: bold;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
    justify-content: space-between;
  }
  .score-add-button {
    margin: 15px;
    height: 50px;
    padding: 10px;
    text-transform: initial;
  }
</style>

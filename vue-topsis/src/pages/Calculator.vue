<script setup lang="ts">
  const personItems = ref([
    {
      name: 'Kurniawan',
      value: 'DAMN',
    },
  ])

  const calcItems = ref([
    {
      text: 'Task closed',
      description: 'Task closed in a month ',
      value: '200',
    },

    {
      text: 'Abcense',
      description: 'The perfect score for the abcense would be 100%',
      value: '88.2 %',
    },

    {
      text: 'Task Completion Rate',
      description: 'Task completion within the set date of the deadline',
      value: '20.3 %',
    },

    {
      text: 'MTTR (Minutes)',
      description: 'The minimum time to recover per tasks',
      value: '124 minutes',
    },
  ])
</script>

<template>
  <v-app class="wallpaper">
    <main>
      <v-container fluid class="calc-container">
        <v-row justify="space-around">
          <v-card class="calc-card" v-for="item in calcItems" :key="item">
            <v-card-title class="font-weight-bold">
              {{ item.text }}
            </v-card-title>
            <v-card-text class="calc-card-text">
              {{ item.value }}
            </v-card-text>
            <v-card-subtitle class="calc-card-desc">
              {{ item.description }}
            </v-card-subtitle>
          </v-card>
        </v-row>
        <v-card class="calc-chart-card">
          <SparkLine />
        </v-card>
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .wallpaper {
    background-color: darkslategrey;
  }

  .calc-container {
    padding: 25px;
    margin-top: 70px;
    background-color: burlywood;
    width: 165vh;
    border-radius: 10px;
  }
  .calc-card {
    padding: 15px;
    margin: 10px;
    background-color: darkslategrey;
    border-radius: 10px;
    height: 20vh;
    width: 38vh;
  }
  .calc-card-text {
    font-weight: bold;
    font-size: 30px;
    margin-top: 20px;
    text-align: top;
  }
  .calc-card-desc {
    text-align: justify;
    vertical-align: bottom;
  }

  .calc-chart-card {
    background-color: darkslategrey;
    border-radius: 10px;
    margin-top: 3vh;
  }
</style>

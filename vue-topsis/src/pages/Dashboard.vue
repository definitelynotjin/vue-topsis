<script setup lang="ts"></script>

<template>
  <v-app class="dashboard-wallpaper">
    <main>
      <v-container fluid class="dashboard-container">
        <v-card class="chart-background" dark>
          <SparkLine />
        </v-card>
      </v-container>
    </main>
  </v-app>
</template>

<style scoped lang="css">
  .dashboard-wallpaper {
    background-color: brown;
  }

  .dashboard-container {
    margin-top: 70px;
    background-color: burlywood;
    width: 165vh;
    border-radius: 10px;
  }

  .chart-background {
    background-color: darkslategrey;
    color: white;
  }
</style>

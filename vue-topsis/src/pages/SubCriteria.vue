<script setup lang="ts"></script>

<template>
  <v-app class="wallpaper">
    <main>
      <v-container fluid class="card-container">
        <v-row justify="space-around"> </v-row>
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
</style>

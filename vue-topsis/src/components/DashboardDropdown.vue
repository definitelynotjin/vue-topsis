<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'

  const projectStore = useProjectStore()
  const emit = defineEmits()
  const props = defineProps<{}>()
</script>

<template>
  <v-container class="dropdown-container">
    <v-card class="base-card">Go to criteria </v-card>
    <v-card class="base-card">Go to alternative </v-card>
    <v-card class="base-card">Go to score </v-card>
  </v-container>
</template>

<style scoped lang="css">
  .dropdown-container {
    background-color: darkblue;
    margin-top: initial;
  }
  .base-card {
    text-align: left;
    padding: 13px;
    height: 50px;
    background-color: darkcyan;
    margin-bottom: 10px;
  }
</style>

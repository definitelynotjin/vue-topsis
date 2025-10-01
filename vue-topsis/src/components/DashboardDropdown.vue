<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useCriteriaStore } from '@/stores/criteriaStore'
  import { useAlternativeStore } from '@/stores/alternativeStore'

  const projectStore = useProjectStore()
  const alternativeStore = useAlternativeStore()
  const criteriaStore = useCriteriaStore()

  const emit = defineEmits()
  const props = defineProps<{}>()
</script>

<template>
  <v-container class="dropdown-container">
    <v-card v-model="criteria" class="base-card">Go to criteria </v-card>
    <v-card v-model="alternative" class="base-card">Go to alternative </v-card>
    <v-card v-model="score" class="base-card">Go to score </v-card>
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

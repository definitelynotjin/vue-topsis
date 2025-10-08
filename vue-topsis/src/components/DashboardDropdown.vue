<script setup lang="ts">
  import { defineProps, defineEmits, onMounted } from 'vue'
  import { useProjectStore } from '@/stores/projectStore'
  import { useScoreStore } from '@/stores/scoreStore'
  import { useAlternativeStore } from '@/stores/alternativeStore'
  import { useCriteriaStore } from '@/stores/criteriaStore'

  const projectStore = useProjectStore()
  const criteriaStore = useCriteriaStore()
  const alternativeStore = useAlternativeStore()
  const scoreStore = useScoreStore()

  const emit = defineEmits()
  const props = defineProps<{ project: any }>()

  onMounted(async () => {
    criteriaStore.loadByProject(projectStore.selectedProjectId)
    alternativeStore.loadByProject(projectStore.selectedProjectId)
    scoreStore.loadByCriteria(projectStore.selectedProjectId, criteriaStore.selectedCriteriaId)
  })
</script>

<template>
  <v-container class="flex flex-1 dropdown-container w-screen">
    <v-row>
      <v-btn
        v-model="projectStore.selectedProjectId"
        :items="criteriaStore.criteria"
        class="base-card"
        >Go to criteria
      </v-btn>
      <v-btn
        v-model="projectStore.selectedProjectId"
        :items="alternativeStore.alternative"
        class="base-card"
        >Go to alternative
      </v-btn>
      <v-btn v-model="projectStore.selectedProjectId" :items="scoreStore.score" class="base-card"
        >Go to score
      </v-btn>
    </v-row>
  </v-container>
</template>

<style scoped lang="css">
  .dropdown-container {
    background-color: red;
  }
  .base-card {
    text-align: left;
    padding: 13px;
    height: 50px;
    background-color: darkcyan;
    margin-bottom: 10px;
  }
</style>

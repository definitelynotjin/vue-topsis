<script setup lang="ts">
  import { Calculator, UserPen, Activity } from 'lucide-vue-next'
  import { useRouter } from 'vue-router'
  import { useProjectStore } from '@/stores/projectStore'

  const props = defineProps({
    project: { type: Object, required: true },
  })
  const router = useRouter()
  const projectStore = useProjectStore()

  function goToCriteria() {
    projectStore.setSelectedProjectId(props.project.id)
    router.push({
      path: '/Criteria',
    })
  }

  function goToAlternative() {
    projectStore.setSelectedProjectId(props.project.id)
    router.push({
      path: '/Alternative',
    })
  }

  function goToScore() {
    projectStore.setSelectedProjectId(props.project.id)
    router.push({
      path: '/ScoringData',
    })
  }
</script>

<template>
  <v-container class="flex goto-container w-screen">
    <v-tooltip text="Go to Criteria">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="Calculator" @click="goToCriteria"> </v-btn>
      </template>
    </v-tooltip>

    <v-tooltip text="Go to alternative">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="UserPen" @click="goToAlternative"> </v-btn>
      </template>
    </v-tooltip>

    <v-tooltip text="Go to score">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="Activity" @click="goToScore"> </v-btn>
      </template>
    </v-tooltip>
  </v-container>
</template>

<style scoped lang="css">
  .goto-container {
    text-align: end;
    justify-content: end;
    justify-items: end;
  }
</style>

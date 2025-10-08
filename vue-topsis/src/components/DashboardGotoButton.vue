<script setup lang="ts">
  import { Calculator, UserPen, Activity } from 'lucide-vue-next'
</script>

<template>
  <v-container class="flex goto-container w-screen">
    <v-tooltip text="Go to Criteria">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="Calculator"> </v-btn>
      </template>
    </v-tooltip>

    <v-tooltip text="Go to alternative">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="UserPen"> </v-btn>
      </template>
    </v-tooltip>

    <v-tooltip text="Go to score">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" :icon="Activity"> </v-btn>
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

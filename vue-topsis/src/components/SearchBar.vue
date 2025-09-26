<script setup lang="ts">
  import { defineEmits } from 'vue'
  const emit = defineEmits(['search'])

  const search = (e) => {
    emit('search', e.target.value)
  }
</script>

<template>
  <v-text-field
    class="searchbar"
    placeholder="Search"
    prepend-inner-icon="mdi-magnify"
    variant="outlined"
    width="100"
    @input="search"
    height="200"
    clearable
    persistent-clear
    flat
    hide-details="auto"
    single-line
  >
  </v-text-field>
</template>

<style scoped lang="css">
  .searchbar {
    margin-top: 14px;
    height: 0.5rem;
  }
</style>

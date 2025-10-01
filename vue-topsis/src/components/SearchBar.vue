<script setup lang="ts">
  import { defineEmits } from 'vue'
  const emit = defineEmits(['search'])

  const search = (e) => {
    emit('search', e.target.value)
  }
</script>

<template>
  <v-text-field
    class="searchbar min-h-auto"
    placeholder="Cari"
    prepend-inner-icon="mdi-magnify"
    variant="outlined"
    width="90"
    @input="search"
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
    margin: 14px;
    height: 30px;
  }
</style>

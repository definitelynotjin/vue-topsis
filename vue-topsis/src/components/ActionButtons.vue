<script setup lang="ts">
  import { Trash, Pen } from 'lucide-vue-next'

  const editItem = (item) => {
    console.log('edit?', item)
  }

  const deleteItem = (item) => {
    console.log('delete?', item)
  }
</script>

<template v-slot:item.actions="{ item }">
  <div class="d-flex justify-end px-10">
    <v-icon color="yellow-darken-3" :icon="Pen" @click="editItem(item.id)"></v-icon>
    <v-icon color="red" :icon="Trash" @click="deleteItem(item.id)"></v-icon>
  </div>
</template>

<style scoped></style>

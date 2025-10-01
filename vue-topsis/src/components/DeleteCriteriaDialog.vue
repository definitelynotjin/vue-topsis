<script setup lang="ts">
  import { Trash } from 'lucide-vue-next'
  import { defineEmits, defineProps } from 'vue'

  const props = defineProps<{
    modelValue: boolean
    criteriaName: string | null
  }>()
  const emit = defineEmits(['update:modelValue', 'confirm-delete'])

  function close() {
    emit('update:modelValue', false)
  }

  function confirm() {
    emit('confirm-delete')
  }
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex">
      <v-row class="justify-around">
        <h1 class="text-xl justify-center font-bold ma-5 pa-5">
          Hapus Kriteria {{ props.criteriaName }} dari Projek ?
        </h1>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons !hover:bg-red-200" @click="confirm" :prepend-icon="Trash"
        >Delete</v-btn
      >
      <v-btn class="action-buttons" @click="close">Cancel</v-btn>
    </v-card-actions>
  </v-dialog>
</template>

<style scoped lang="css">
  .dialog-card {
    border-radius: 10px;
  }

  .action-buttons {
    font-size: 15px;
    text-transform: initial;
  }
</style>

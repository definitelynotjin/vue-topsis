<script setup lang="ts">
  import { Trash } from 'lucide-vue-next'
  import { defineEmits, defineProps } from 'vue'

  const props = defineProps<{
    modelValue: boolean
    alternativeName: string | null
    projectId: number | null
    projectName: string | null
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
        <h1 class="text-xl justify-center ma-5 pa-5">
          Hapus Seluruh Data Projek
          <strong>
            {{ props.projectName }}
          </strong>
          ?
        </h1>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons-delete" @click="confirm" :prepend-icon="Trash">Delete</v-btn>
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

  .action-buttons-delete {
    font-size: 15px;
    text-transform: initial;
    background-color: red;
    color: white;
  }
</style>

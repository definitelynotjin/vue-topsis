<script setup lang="ts">
  import { Trash } from 'lucide-vue-next'
  import { defineEmits, defineProps } from 'vue'

  const props = defineProps<{
    modelValue: boolean
    scoreName: string | null
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
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Hapus Score dari Projek ?</h1>
      </v-col>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons" @click="confirm" :prepend-icon="Trash">Delete</v-btn>
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

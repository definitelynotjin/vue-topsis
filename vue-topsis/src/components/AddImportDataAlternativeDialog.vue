<script setup lang="ts">
  import { Save } from 'lucide-vue-next'
  import { defineProps, defineEmits } from 'vue'
  import { toast } from 'vue-sonner'

  const emit = defineEmits(['update:modelValue', 'saved'])

  const props = defineProps<{
    modelValue: boolean
  }>()

  function close() {
    emit('update:modelValue', false)
  }

  function importData() {}
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-file-upload
        class="file-upload"
        browse-text="Browse Files"
        divider-text="or"
        title="Drag and drop the file here"
        :style="{ bgColor: 'cyan-darken-1' }"
        style="background-color: transparent"
        clearable
      >
      </v-file-upload>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons" @click="importData" :prepend-icon="Save">Import</v-btn>
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
  .file-upload-card {
    background-color: gray;
  }
  .file-upload {
    justify-content: center;
    justify-items: stretch;
    color: red;
  }
</style>

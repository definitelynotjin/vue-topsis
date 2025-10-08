<script setup lang="ts">
  import { Save } from 'lucide-vue-next'
  import { defineProps, defineEmits } from 'vue'
  import { toast } from 'vue-sonner'
  import { useAlternativeStore } from '@/stores/alternativeStore'

  const alternativeStore = useAlternativeStore()
  const selectedFile = ref<File | null>(null)

  const emit = defineEmits(['update:modelValue', 'imported'])
  const props = defineProps<{
    modelValue: boolean
    project_id: number
  }>()

  function close() {
    emit('update:modelValue', false)
  }

  function handleFileUpload(files: File | File[]) {
    if (Array.isArray(files) && files.length > 0) {
      selectedFile.value = files[0]
    } else if (files instanceof File) {
      selectedFile.value = files
    } else {
      selectedFile.value = null
    }
  }

  async function importData() {
    if (!selectedFile.value) {
      console.error('this is why you cannot upload')
      toast.error('sorry biig bro, some aint right')
      return
    }
    try {
      await alternativeStore.importAlternative(props.project_id, selectedFile.value)
      emit('imported')
      close()
      selectedFile.value = null
    } catch (error) {
      console.error('damn somethin wrong', error)
      toast.error('something wrong big bro in the import')
    }
  }
</script>

<template>
  <v-dialog
    :model-value="props.modelValue"
    @update:model-value="(val) => emit('update:modelValue', val)"
    class="max-w-200 dialog-wallpaper justify-center"
  >
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-file-input
        @update:model-value="handleFileUpload"
        class="file-upload"
        accept=".xlsx"
        clearable
        title="Drag and drop"
        style="background-color: transparent"
      >
      </v-file-input>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons !bg-cyan-700" @click="importData" :prepend-icon="Save"
        >Import</v-btn
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
  .file-upload-card {
    background-color: gray;
  }
  .file-upload {
    justify-content: center;
    justify-items: stretch;
  }
</style>

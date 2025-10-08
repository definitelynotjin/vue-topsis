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

  function handleFileUpload(files: File[]) {
    if (files && files.length < 0) {
      selectedFile.value = files[0]
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
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-file-upload
        class="file-upload"
        browse-text="Browse Files"
        divider-text="or"
        title="Drag and drop the file here"
        style="background-color: transparent"
        clearable
        @update:model-value="handleFileUpload"
      >
      </v-file-upload>
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
    color: red;
  }
</style>

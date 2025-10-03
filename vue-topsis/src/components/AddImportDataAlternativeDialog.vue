<script setup lang="ts">
  import { Save } from 'lucide-vue-next'
  import { ref, defineProps, defineEmits } from 'vue'
  import { toast } from 'vue-sonner'

  const emit = defineEmits(['update:modelValue', 'saved'])
  const onAdvancedUpload = () => {
    toast.warning('damn')
  }
  const props = defineProps<{
    modelValue: boolean
  }>()
  function close() {
    emit('update:modelValue', false)
  }
  function save() {}
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Add new Project</h1>
        <div class="file-upload-card">
          <FileUpload
            accept="image/*"
            :max-file-size="10000000"
            class="file-upload"
            name="demo[]"
            @upload="onAdvancedUpload"
            :multiple="true"
          >
            <template #empty>
              <span>Enter file or drag and drop something</span>
            </template>
          </FileUpload>
        </div>
      </v-col>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons" @click="save" :prepend-icon="Save">Save</v-btn>
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

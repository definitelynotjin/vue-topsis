<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useProjectStore } from '../stores/projectStore'
  import { toast } from 'vue-sonner'

  const projectStore = useProjectStore()
  const projectName = ref('')
  const projectDescription = ref('')

  const props = defineProps<{
    modelValue: boolean
  }>()
  const emit = defineEmits(['update:modelValue', 'saved'])

  function close() {
    emit('update:modelValue', false)
  }
  async function save() {
    if (!projectName.value || !projectDescription.value) {
      toast.error('Project name or description must be inserted')
      return
    }
    try {
      await projectStore.addProject({
        name: projectName.value,
        description: projectDescription.value,
      })
      emit('saved')
      close()
      projectName.value = ''
      projectDescription.value = ''
    } catch (error) {
      console.error(error)
      toast.error('sopmething wong')
    }
  }
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Add new Project</h1>
        <v-text-field v-model="projectName" variant="outlined" placeholder="Enter project name" />

        <v-text-field
          v-model="projectDescription"
          variant="outlined"
          placeholder="Enter project description"
        />
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
</style>

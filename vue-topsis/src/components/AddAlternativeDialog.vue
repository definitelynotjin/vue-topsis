<script setup lang="ts">
  import { defineProps, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useAlternativeStore } from '@/stores/alternativeStore'

  const alternativeStore = useAlternativeStore()

  const alternativeName = ref('')
  const alternativeId = ref(null)

  const props = defineProps<{
    modelValue: boolean
    project_id: number
  }>()
  const emit = defineEmits(['update:modelValue', 'saved'])
  function close() {
    emit('update:modelValue', false)
  }

  async function save() {
    if (!alternativeId.value || !alternativeName.value) {
      alert('All rquired eh')
      return
    }
    try {
      await alternativeStore.addAlternative({
        id_alt: alternativeId.value,
        name: alternativeName.value,
        project_id: props.project_id,
      })
      emit('saved')
      close()
      alternativeName.value = ''
      alternativeId.value = null
    } catch (error) {
      console.error(error)
      alert('sopmething wong')
    }
  }
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 justify-center">
    <v-card-text class="dialog-card bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Enter new Alternative</h1>
        <v-text-field
          v-model="alternativeName"
          variant="outlined"
          placeholder="Enter new alternative"
        />
        <v-text-field
          v-model="alternativeId"
          variant="outlined"
          placeholder="Enter alternative ID"
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

<style scoped>
  .dialog-card {
    border-radius: 10px;
  }
  .action-buttons {
    text-transform: initial;
  }
</style>

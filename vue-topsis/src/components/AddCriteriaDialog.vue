<script setup lang="ts">
  import { defineProps, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useCriteriaStore } from '@/stores/criteriaStore'

  const criteriaStore = useCriteriaStore()
  const criteriaName = ref('')
  const criteriaType = ref('')
  const criteriaWeight = ref<number | null>(null)

  const props = defineProps<{
    modelValue: boolean
    projectId: number
  }>()
  const emit = defineEmits(['update:modelValue', 'saved'])
  function close() {
    emit('update:modelValue', false)
  }
  async function save() {
    if (!criteriaName.value || !criteriaType.value || !criteriaWeight.value) {
      alert('All rquired eh')
      return
    }
    try {
      await criteriaStore.addCriteria({
        project_id: props.projectId,
        name: criteriaName.value,
        type: criteriaType.value.toLowerCase(),
        weight: criteriaWeight.value,
      })
      emit('saved')
      close()
      criteriaName.value = ''
      criteriaWeight.value = null
      criteriaType.value = ''
    } catch (error) {
      console.error(error)
      alert('sopmething wong')
    }
  }
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Enter new Criteria</h1>
        <v-text-field v-model="criteriaName" variant="outlined" placeholder="Enter criteria name" />
        <v-combobox
          variant="outlined"
          v-model="criteriaType"
          label="Enter criteria type"
          placeholder="Enter criteria type"
          :items="['Benefit', 'Cost']"
          :list-props="{ bgColor: 'cyan-darken-2' }"
        />
        <v-text-field v-model="criteriaWeight" placeholder="Enter criteria weight " />
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
    font-size: 15px;
    text-transform: initial;
  }
</style>

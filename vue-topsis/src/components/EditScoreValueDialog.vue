<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useScoreStore } from '../stores/scoreStore'
  import { toast } from 'vue-sonner'

  const scoreStore = useScoreStore()
  const scoreName = ref('')
  const scoreType = ref('')
  const scoreValue = ref<number | null>(null)
  const scoreWeight = ref<number | null>(null)

  const props = defineProps<{
    modelValue: boolean
    alternativeId: number
  }>()

  const emit = defineEmits(['update:modelValue', 'saved'])
  function close() {
    emit('update:modelValue', false)
  }
  async function save() {
    if (!scoreName.value || !scoreType.value || !scoreWeight.value) {
      toast.error('Score value must be inserted')
      return
    }
    try {
      await scoreStore.addScore({
        alternative_id: props.alternativeId,
        value: scoreValue.value,
      })
      emit('saved')
      close()
      scoreValue.value = null
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
        <h1 class="text-xl font-bold mb-5">Edit new Value</h1>
        <v-text-field
          v-model="scoreName"
          readonly
          variant="outlined"
          placeholder="Enter score name"
        />
        <v-combobox
          readonly
          variant="outlined"
          v-model="scoreType"
          label="Enter score type"
          placeholder="Enter score type"
          :items="['Benefit', 'Cost']"
          :list-props="{ bgColor: 'cyan-darken-2' }"
        />
        <v-text-field readonly v-model="scoreWeight" placeholder="Enter score weight " />
        <v-text-field readonly v-model="scoreValue" placeholder="Enter score value " />
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

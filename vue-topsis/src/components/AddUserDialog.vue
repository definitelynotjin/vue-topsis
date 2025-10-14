<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useUserStore } from '../stores/userStore.ts'
  import { toast } from 'vue-sonner'

  const userStore = useUserStore()
  const userName = ref('')
  const userPass = ref('')
  const userRole = ref('')

  const props = defineProps<{
    modelValue: boolean
  }>()
  const emit = defineEmits(['update:modelValue', 'saved'])

  function close() {
    emit('update:modelValue', false)
  }
  async function save() {
    if (!userName.value || !userRole.value) {
      toast.error('All fields must be filled')
      return
    }
    try {
      await userStore.registerUser({
        username: userName.value,
        password: userPass.value,
        role: userRole.value.toLowerCase(),
      })
      emit('saved')
      close()
      userName.value = ''
      userPass.value = ''
      userRole.value = ''
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
        <h1 class="text-xl font-bold mb-5">Add new User</h1>
        <v-text-field v-model="userName" variant="outlined" placeholder="Enter username" />
        <v-text-field v-model="userPass" variant="outlined" placeholder="Enter password" />
        <v-combobox
          variant="outlined"
          v-model="userRole"
          label="Enter user role"
          placeholder="Enter user role"
          :items="['Admin', 'User']"
          :list-props="{ bgColor: 'cyan-darken-2' }"
        />
      </v-col>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn class="action-buttons !bg-cyan-700" @click="save" :prepend-icon="Save">Save</v-btn>
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

<script setup lang="ts">
  import { defineProps, ref, defineEmits } from 'vue'
  import { Save } from 'lucide-vue-next'
  import { useUserStore } from '../stores/userStore'
  import { toast } from 'vue-sonner'

  const userStore = useUserStore()

  const props = defineProps<{
    userId: number
    modelValue: boolean
    userName: string
    userPass: string
    userRole: string
  }>()

  const userName = ref(props.userName)
  const userPass = ref(props.userPass)
  const userRole = ref(props.userRole)

  async function handleUserEdit() {
    if (!props.userId) return

    try {
      await userStore.editUser(props.userId, {
        username: props.userName,
        password: props.userPass,
        role: props.userRole,
      })
      toast.success('User has been edited successfully')
      emit('saved')
      close()
      await userStore.loadAllUsers()
    } catch (error) {
      console.error('canpt edit erh', error)
      throw error
    }
  }

  const emit = defineEmits(['update:modelValue', 'saved'])

  function close() {
    emit('update:modelValue', false)
  }

  watch(
    () => [props.userName, props.userPass, props.userRole],
    ([username, password, role]) => {
      userName.value = username
      userPass.value = password
      userRole.value = role
    },
  )
</script>

<template>
  <v-dialog v-model="props.modelValue" class="max-w-200 dialog-wallpaper justify-center">
    <v-card-text class="dialog-card !bg-cyan-700 flex justify-center">
      <v-col class="" cols="6" md="6" sm="8">
        <h1 class="text-xl font-bold mb-5">Edit User information</h1>
        <v-text-field v-model="userName" variant="outlined" placeholder="Enter username" />
        <v-text-field
          v-model="userPass"
          variant="outlined"
          placeholder="Enter password"
          type="password"
        />
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
      <v-btn class="action-buttons !bg-cyan-700" @click="handleUserEdit" :prepend-icon="Save"
        >Edit</v-btn
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
</style>

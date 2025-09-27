<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  // import { useToast } from '@/components/ui/toast/use-toast'

  // const { toast } = useToast()
  const router = useRouter()
  const username = ref('')
  const password = ref('')
  const show1 = ref(false)
  const valid = ref(false)

  const nameRules = [
    (v: string) => !!v || 'Username is required',
    (v: string) => (v && v.length <= 10) || 'Username must be less than 10 characters',
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password is required',
    (v: string) => (v && v.length <= 6) || 'Password must be less than 6 characters',
  ]

  function handleLogin() {
    if (username.value === 'Admin' && password.value === '1234') {
      localStorage.setItem('isLoggedIn', 'true')
      router.push('/dashboard')
    } else {
      // toast({
      //   title: 'Invalid Credentials!',
      //   description: 'Make sure you inserted the username or password correctly',
      //   variant: 'destructive',
      // })
    }
  }
</script>

<template>
  <v-app class="!bg-gradient-to-r from-cyan-400 to-violet-600 hide-scrollbar">
    <v-row class="ma-10 pa-10">
      <v-col class="bg-gray-900 rounded-tl-2xl rounded-bl-2xl d-flex">
        <v-row align="center">
          <v-img :height="150" :width="150" />
        </v-row>
      </v-col>
      <v-col class="bg-slate-100 rounded-tr-2xl rounded-br-2xl flex items-center justify-center">
        <v-form
          v-model="valid"
          class="w-full !text-gray-900 flex flex-col gap-4 max-w-md"
          @submit.prevent="handleLogin"
        >
          <h1 class="text-h3 font-bold text-gray-700">Login</h1>
          <h2 class="top-auto text-gray-500">Enter your user valid username and password.</h2>
          <v-text-field
            v-model="username"
            class="form-color"
            bg-color="cyan-darken-1"
            :counter="10"
            label="Username"
            required
            :rules="nameRules"
            variant="solo"
          />

          <v-text-field
            v-model="password"
            class="form-color"
            :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            bg-color="cyan-darken-1"
            :counter="6"
            :elevation="24"
            label="Password"
            required
            :rules="passwordRules"
            :type="show1 ? 'text' : 'password'"
            variant="solo"
            @click:append-inner="show1 = !show1"
          />

          <v-btn
            bg="red-darken-2"
            class="!bg-cyan-700 submit-button"
            density="comfortable"
            :height="50"
            rounded="lg"
            type="submit"
            variant="tonal"
          >
            Submit
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-app>
</template>
<style scoped lang="css">
  .form-color {
    color: green;
  }
  .submit-button {
    color: white;
    text-transform: initial;
  }
  .v-row.hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
</style>

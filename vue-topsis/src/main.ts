/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

import * as VInlineFields from '@wdns/vuetify-inline-fields'

import { FileUpload } from 'primevue'
import PrimeVue from 'primevue/config'
// Composables
import { createApp } from 'vue'
// Plugins
import { registerPlugins } from '@/plugins'
// Components
import App from './App.vue'

// Styles
import 'unfonts.css'
import './styles/main.css'
import '@fontsource-variable/open-sans'
import './styles/overrides.css'

const app = createApp(App)
for (const prop in VInlineFields) {
  app.component(prop, VInlineFields[prop])
}

registerPlugins(app)

app.mount('#app')
app.use(PrimeVue)
app.component('FileUpload', FileUpload)

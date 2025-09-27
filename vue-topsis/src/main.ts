/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

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

registerPlugins(app)

app.mount('#app')
// app.use(Toast)

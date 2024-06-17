import { createApp } from 'vue'
import './style.css'
import router from './routers/router'
import App from './App.vue'
import { Skeletor } from 'vue-skeletor';

import 'vue-skeletor/dist/vue-skeletor.css';

const app = createApp(App);
app.use(router)
app.component(Skeletor.name, Skeletor);
app.mount('#app')
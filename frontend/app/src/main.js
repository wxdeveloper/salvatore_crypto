import { createApp } from 'vue'
import './style.css'
import router from './routers/router'
import App from './App.vue'
import { Skeletor } from 'vue-skeletor';

import 'vue-skeletor/dist/vue-skeletor.css';
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { BiDiscord, BiGithub, BiTwitter } from "oh-vue-icons/icons";

addIcons(BiDiscord, BiGithub, BiTwitter);

const app = createApp(App);
app.use(router)
app.component(Skeletor.name, Skeletor);
app.component("v-icon", OhVueIcon);
app.mount('#app')
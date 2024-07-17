import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = ' http://127.0.0.1:8000/'
// axios.defaults.baseURL = 'http://10.90.138.241:8000/'

const app = createApp(App);
app.use(router);
app.config.globalProperties.$axios = axios;  // если нужно использовать axios глобально
app.mount('#app');


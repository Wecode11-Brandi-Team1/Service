import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify.js'
import VueAxios from './plugins/axios.js'
import { router } from './routes/index.js'
import { store } from './store.js'
import "./style/reset.scss";

Vue.use(VueAxios);
Vue.config.productionTip = false

new Vue({
  render: (h) => h(App),
  router,
  vuetify,
  store: store,
}).$mount("#app");
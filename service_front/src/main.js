import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify.js'
import VueAxios from "./plugins/axios.js"
import VueDaumPostcode from "vue-daum-postcode"
import VueCookies from "vue-cookies"
import { router } from './routes/index.js'
import { store } from './store.js'
import "./style/reset.scss";

Vue.use(VueAxios);
Vue.use(VueDaumPostcode);
Vue.use(VueCookies);

Vue.config.productionTip = false
Vue.$cookies.config("1d");

new Vue({
  render: (h) => h(App),
  router,
  vuetify,
  store: store,
}).$mount("#app");
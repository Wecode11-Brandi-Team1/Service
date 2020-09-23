import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    isGoogle: false,
    token: "",
    googleToken: "",
    resultSelected: "",
    resultTotal: "",
    cancelTotal: "",
    signUpTabName: "",
    myPageTabName: "",
    myPageShow: true,
  },
});

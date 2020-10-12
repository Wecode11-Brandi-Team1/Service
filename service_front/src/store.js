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
    categoryShop: [],
    categoryBrand: [],
    categoryBeauty: [],
    selected: 0, 
    menutab: {
      currentHover: 0,
      activeTab: 0,
    },
    showModal: false,
    couponNum: "",
    mobilePageName: "",
    isMypage: false,
    isTabBar:""
  },
});

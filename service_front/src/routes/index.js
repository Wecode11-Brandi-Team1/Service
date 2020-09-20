import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main/Main.vue'
import Login from '../views/Login/Login.vue'
import Signup from '../views/Signup/Signup.vue'
import ProductList from '../views/ProductList/ProductList.vue'
import ProductDetail from '../views/ProductDetail/ProductDetail.vue'
import Cart from '../views/Cart/Cart.vue'
import Order from '../views/Order/Order.vue'
import Mypage from '../views/Mypage/Mypage.vue'
import Event from '../views/Event/Event.vue'
import GSignInButton from 'vue-google-signin-button'

Vue.use(VueRouter)
Vue.use(GSignInButton)

export const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'Main',
            component: Main
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/signup',
            name: 'Signup',
            component: Signup
        },
        {
            path: '/productList',
            name: 'ProductList',
            component: ProductList
        },
        {
            path: '/productDetail',
            name: 'ProductDetail',
            component: ProductDetail
        },
        {
            path: '/cart',
            name: 'Cart',
            component: Cart
        },
        {
            path: '/order',
            name: 'Order',
            component: Order
        },
        {
            path: '/mypage',
            name: 'Mypage',
            component: Mypage
        },
        {
            path: '/event',
            name: 'Event',
            component: Event
        },
    ]
})
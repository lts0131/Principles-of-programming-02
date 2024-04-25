import Vue from 'vue'
import Router from 'vue-router'
import login from '@/pages/login'
import admin from '@/pages/admin'
import user from '@/pages/user'

Vue.use(Router)

export default new Router({
    routes: [{
        path: '/',
        name: 'index',
        component: login
    }, {
        path: '/admin',
        name: 'admin',
        component: admin
    }, {
        path: '/user',
        name: 'user',
        component: user
    }]
})

import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "about" */ '../views/About.vue'),
    },
    {
        path: '/auth/login',
        name: 'Login',
        component: () => import('../views/auth/Login.vue'),
    },
    {
        path: '/classrooms',
        name: 'Classrooms',
        meta: { requiresAuth: true },
        component: () => import('../views/Classrooms.vue'),
    },
    {
        path: '/classrooms/detail',
        name: 'Detail',
        props: true,
        meta: { requiresAuth: true },
        component: () => import('../views/Detail.vue'),
        children: [
            {
                path: ':classroom_id/',
                name: 'Overview',
                props: true,
                meta: { requiresAuth: true },
                component: () => import('../views/Overview.vue'),
            },
            {
                path: ':classroom_id/rooms',
                name: 'Rooms',
                props: true,
                meta: { requiresAuth: true },
                component: () => import('../views/Rooms.vue'),
            },
            {
                path: ':classroom_id/discussion',
                name: 'Discussion',
                props: true,
                meta: { requiresAuth: true },
                component: () => import('../views/Discussion.vue'),
            },
        ],
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('user')

    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!loggedIn) {
            next({
                path: '/auth/login',
                query: { redirect: to.fullPath },
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})

export default router

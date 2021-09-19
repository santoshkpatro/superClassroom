import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from '../views/Dashboard.vue'
import ClassroomList from '../views/ClassroomList.vue'

// Auth Components
import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'

// Dashboard Components
import Overview from '../views/dashboard/Overview.vue'
import Other from '../views/dashboard/Other.vue'
import RoomList from '../views/dashboard/RoomList.vue'
import AssignmentList from '../views/dashboard/AssignmentList.vue'

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
        component: Login,
    },
    {
        path: '/auth/register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/classrooms',
        name: 'ClassroomList',
        component: ClassroomList,
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: { requiresAuth: true },
        children: [
            {
                path: ':classroom_id',
                name: 'Overview',
                props: true,
                component: Overview,
            },
            {
                path: ':classroom_id/other',
                name: 'Other',
                props: true,
                component: Other,
            },
            {
                path: ':classroom_id/rooms',
                name: 'RoomList',
                props: true,
                component: RoomList,
            },
            {
                path: ':classroom_id/assignments',
                name: 'AssignmentList',
                props: true,
                component: AssignmentList,
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

    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
        next('/auth/login')
    }
    next()
})

export default router

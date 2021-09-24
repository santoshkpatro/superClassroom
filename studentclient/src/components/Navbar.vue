<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <router-link class="navbar-brand" :to="{ name: 'Home' }"
                >Super Classroom</router-link
            >
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link
                            class="nav-link"
                            :to="{ name: 'Classrooms' }"
                            >Classrooms</router-link
                        >
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'About' }"
                            >About</router-link
                        >
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item" v-if="!loggedIn">
                        <router-link
                            class="btn btn-sm btn-primary mx-2"
                            :to="{ name: 'Login' }"
                            >Login</router-link
                        >
                    </li>
                    <li class="nav-item" v-if="loggedIn">
                        <a href="#" class="nav-link">Hi, {{ getUserName }}</a>
                    </li>
                    <li class="nav-item" v-if="loggedIn">
                        <button
                            class="btn btn-sm btn-secondary mx-2"
                            @click="handleLogout"
                        >
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Navbar',
    computed: {
        ...mapGetters(['loggedIn', 'getUserName']),
    },
    methods: {
        handleLogout() {
            this.$store.dispatch('logout')
        },
    },
}
</script>

<style>
</style>
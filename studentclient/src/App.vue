<template>
    <div>
        <!-- <Navbar /> -->
        <router-view></router-view>
        <div class="container-fluid">
            <div class="row">
                <nav
                    id="sidebarMenu"
                    class="
                        col-md-3 col-lg-3
                        d-md-block
                        bg-light
                        sidebar
                        collapse
                    "
                >
                    <router-view name="sidebar"></router-view>
                </nav>
                <main class="col-md-9 ms-sm-auto col-lg-9 px-md-4">
                    <router-view name="main"></router-view>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Navbar from './components/Navbar.vue'

export default {
    components: {
        Navbar,
    },
    created() {
        const userString = localStorage.getItem('user')
        if (userString) {
            const userData = JSON.parse(userString)
            this.$store.commit('SET_USER_DATA', userData)
        }
        axios.interceptors.response.use(
            (response) => response,
            (error) => {
                if (error.response.status === 401) {
                    this.$store.dispatch('logout')
                }
                return Promise.reject(error)
            }
        )
    },
}
</script>

<style>
.sidebar {
    /* position: fixed; */
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 100; /* Behind the navbar */
    padding: 48px 0 0; /* Height of navbar */
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.1);
}

@media (max-width: 767.98px) {
    .sidebar {
        top: 5rem;
    }
}

.sidebar-sticky {
    position: relative;
    top: 0;
    height: calc(100vh - 48px);
    padding-top: 0.5rem;
    overflow-x: hidden;
    overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

.sidebar .nav-link {
    font-weight: 500;
    color: #333;
}

.sidebar .nav-link .feather {
    margin-right: 4px;
    color: #727272;
}

.sidebar .nav-link.active {
    color: #2470dc;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
    color: inherit;
}

.sidebar-heading {
    font-size: 0.75rem;
    text-transform: uppercase;
}

.form-control-dark {
    color: #fff;
    background-color: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.1);
}

.form-control-dark:focus {
    border-color: transparent;
    box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.25);
}
</style>

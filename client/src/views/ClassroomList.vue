<template>
    <div class="container">
        <Navbar />
        <div class="box" v-for="classroom in classrooms" :key="classroom.id">
            <router-link
                :to="{
                    name: 'Overview',
                    params: { classroom_id: classroom.id },
                }"
            >
                <p>
                    {{ classroom.name }}
                </p>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Navbar from '../components/Navbar.vue'

export default {
    components: { Navbar },
    data() {
        return {
            classrooms: null,
        }
    },
    created() {
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/classrooms/list/`)
            .then(({ data }) => (this.classrooms = data))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>
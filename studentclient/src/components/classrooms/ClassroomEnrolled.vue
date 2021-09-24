<template>
    <div>
        <div v-if="isLoading">
            <Loader />
        </div>
        <div v-else>
            <h1>Fetch Complete</h1>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Loader from '@/components/Loader.vue'

export default {
    name: 'ClassroomEnrolled',
    components: { Loader },
    data() {
        return {
            isLoading: false,
            classrooms: null,
        }
    },
    mounted() {
        this.isLoading = true
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/classrooms/list`)
            .then(({ data }) => {
                this.classrooms = data
                this.isLoading = false
            })
            .catch((e) => {
                console.log(e)
                this.isLoading = false
            })
    },
}
</script>

<style>
</style>
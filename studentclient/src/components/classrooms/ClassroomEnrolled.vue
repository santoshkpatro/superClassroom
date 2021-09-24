<template>
    <div>
        <div v-if="isLoading">
            <Loader />
        </div>
        <div v-else>
            <div class="row">
                <div
                    class="col-6 card"
                    v-for="classroom in classrooms"
                    :key="classroom.id"
                >
                    <img
                        src="https://avatars.dicebear.com/api/identicon/random.svg"
                        class="card-img-top"
                        alt="#"
                        height="200"
                        width="200"
                    />
                    <div class="card-body">
                        <h5 class="card-title">{{ classroom.name }}</h5>
                        <p class="card-text">
                            {{ classroom.description }}
                        </p>
                        <router-link
                            :to="{
                                name: 'Overview',
                                params: { classroom_id: classroom.id },
                            }"
                            class="btn btn-primary"
                            >Check Details</router-link
                        >
                    </div>
                </div>
            </div>
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
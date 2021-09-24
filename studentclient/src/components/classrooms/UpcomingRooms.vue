<template>
    <div>
        <div v-if="isLoading">
            <Loader />
        </div>
        <div v-else>
            <h3 class="text-center">Recent Rooms</h3>
            <UpcomingRoomCard
                v-for="room in rooms"
                :key="room.id"
                :room="room"
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Loader from '@/components/Loader.vue'
import UpcomingRoomCard from '@/components/classrooms/UpcomingRoomCard.vue'

export default {
    name: 'UpcomingRooms',
    components: {
        Loader,
        UpcomingRoomCard,
    },
    data() {
        return {
            isLoading: false,
            rooms: null,
        }
    },
    mounted() {
        this.isLoading = true
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/classrooms/rooms/`)
            .then(({ data }) => {
                this.rooms = data
                this.isLoading = false
            })
            .catch((e) => {
                this.isLoading = false
                console.log(e)
            })
    },
}
</script>

<style>
</style>
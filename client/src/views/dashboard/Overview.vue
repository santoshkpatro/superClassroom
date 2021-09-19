<template>
    <h1>Overview</h1>
</template>

<script>
import axios from 'axios'

export default {
    props: ['classroom_id'],
    data() {
        return {
            rooms: null,
            assignments: null,
            notes: null,
        }
    },
    created() {
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/rooms/list`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => (this.rooms = data))
            .catch((e) => console.log(e))

        axios
            .get(`${process.env.VUE_APP_API_URL}/api/assignments/list/`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => (this.assignments = data))
            .catch((e) => console.log(e))

        axios
            .get(`${process.env.VUE_APP_API_URL}/api/notes/list`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => (this.notes = data))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>
<template>
    <div>
        <div class="box" v-for="note in notes" :key="note.id">
            {{ note.title }}
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    props: ['classroom_id'],
    data() {
        return {
            notes: null,
        }
    },
    created() {
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/notes/list/`, {
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
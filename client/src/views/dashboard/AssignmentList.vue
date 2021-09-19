<template>
    <div>
        <div class="box" v-for="assignment in assignments" :key="assignment.id">
            {{ assignment.title }}
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    props: ['classroom_id'],
    data() {
        return {
            assignments: null,
        }
    },
    created() {
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/assignments/list`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => (this.assignments = data))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>
<template>
    <div>
        <AssignmentCard
            v-for="assignment in assignments"
            :key="assignment.id"
            :assignment="assignment"
        />
    </div>
</template>

<script>
import axios from 'axios'
import AssignmentCard from '../../components/assignments/AssignmentCard.vue'

export default {
    props: ['classroom_id'],
    components: {
        AssignmentCard,
    },
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
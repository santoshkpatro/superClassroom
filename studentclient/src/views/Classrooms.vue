<template>
    <div class="container">
        <div>
            <h1>Classroom</h1>
            <ClassroomEnrolled />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ClassroomEnrolled from '@/components/classrooms/ClassroomEnrolled.vue'

export default {
    name: 'Classrooms',
    components: {
        ClassroomEnrolled,
    },
    data() {
        return {}
    },
    mounted() {},
}
</script>

<style>
</style>
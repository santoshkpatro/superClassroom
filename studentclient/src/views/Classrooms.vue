<template>
    <div class="container">
        <div>
            <h1>Classroom</h1>
            <div class="row">
                <div class="col">
                    <ClassroomEnrolled />
                </div>
                <div class="col">
                    <div class="card">
                        <UpcomingRooms />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ClassroomEnrolled from '@/components/classrooms/ClassroomEnrolled.vue'
import UpcomingRooms from '@/components/classrooms/UpcomingRooms.vue'

export default {
    name: 'Classrooms',
    components: {
        ClassroomEnrolled,
        UpcomingRooms,
    },
    data() {
        return {}
    },
    mounted() {},
}
</script>

<style>
</style>
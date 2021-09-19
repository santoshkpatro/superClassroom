<template>
    <div>
        <div class="columns">
            <div class="column is-one-quarter">
                <Sidebar :classroomId="classroomId" />
            </div>
            <div class="column">
                <Menu />
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar.vue'
import Menu from '../components/Menu.vue'

export default {
    components: { Sidebar, Menu },
    data() {
        return {
            classroomId: null,
        }
    },
    created() {
        this.classroomId = this.$route.params.classroom_id
    },
}
</script>

<style>
</style>
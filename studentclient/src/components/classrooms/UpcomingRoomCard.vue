<template>
    <div>
        <h5>{{ room.title }}</h5>
        <p>Schedule On: {{ room.schedule_on }}</p>
        <a :href="room.url" target="_blank">Click Here to Join</a>
    </div>
</template>

<script>
export default {
    name: 'UpcomingRoomCard',
    props: ['room'],
    mounted() {},
}
</script>

<style>
</style>
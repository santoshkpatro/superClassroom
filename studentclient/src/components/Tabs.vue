<template>
    <ul class="nav">
        <li class="nav-item">
            <router-link
                class="nav-link"
                :to="{
                    name: 'Overview',
                    params: { classroom_id: $route.params.classroom_id },
                }"
                >Overview</router-link
            >
        </li>
        <li class="nav-item">
            <router-link
                class="nav-link"
                :to="{
                    name: 'Rooms',
                    params: { classroom_id: $route.params.classroom_id },
                }"
                >Rooms</router-link
            >
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Assignments</a>
        </li>
        <li class="nav-item">
            <a class="nav-link">Notes</a>
        </li>
        <li class="nav-item">
            <router-link
                class="nav-link"
                :to="{
                    name: 'Discussion',
                    params: { classroom_id: $route.params.classroom_id },
                }"
                >Discussion</router-link
            >
        </li>
    </ul>
</template>

<script>
export default {
    name: 'Tabs',
}
</script>

<style scoped>
li a {
    text-decoration: none;
    color: black;
}

.router-link-active {
    border-bottom: 2px solid black;
}
</style>
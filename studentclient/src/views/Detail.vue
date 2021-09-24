<template>
    <div class="container mt-5">
        <Tabs />
        <router-view class="mt-2"></router-view>
    </div>
</template>

<script>
import Tabs from '@/components/Tabs.vue'

export default {
    name: 'Detail',
    components: {
        Tabs,
    },
    props: ['classroom_id'],
}
</script>

<style>
</style>
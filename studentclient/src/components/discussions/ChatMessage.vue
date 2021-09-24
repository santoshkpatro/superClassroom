<template>
    <li
        class="clearfix"
        :class="{
            agent: getUser.id !== chat.user.id,
            self: getUser.id === chat.user.id,
        }"
    >
        <span
            class="chat-img left clearfix mx-2"
            v-if="getUser.id !== chat.user.id"
        >
            <img
                src="http://placehold.it/50/55C1E7/fff&text=U"
                alt="Agent"
                class="img-circle"
            />
        </span>
        <div class="chat-body clearfix">
            <div class="header clearfix">
                <strong
                    class="primary-font"
                    v-if="getUser.id !== chat.user.id"
                    >{{ chat.user.name }}</strong
                >
                <small
                    class="text-muted"
                    :class="{
                        right: getUser.id !== chat.user.id,
                        left: getUser.id === chat.user.id,
                    }"
                >
                    <span
                        class="glyphicon glyphicon-time"
                        :class="{ 'ms-4': getUser.id !== chat.user.id }"
                    ></span
                    >14 mins ago</small
                >
            </div>
            <p>{{ chat.message }}</p>
        </div>
    </li>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'ChatMessage',
    props: ['chat'],
    computed: {
        ...mapGetters(['getUser']),
    },
}
</script>

<style>
</style>
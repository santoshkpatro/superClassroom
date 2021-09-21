<template>
    <div>
        <h1>Chat</h1>
        <div>
            <div v-for="chat in chats" :key="chat.id">
                <div class="columns">
                    <div class="column is-half">
                        <div class="box" v-if="chat.user.id !== getUser.id">
                            <p class="has-text-weight-bold">
                                {{ chat.user.name }}
                            </p>
                            <p>{{ chat.message }}</p>
                        </div>
                    </div>
                    <div class="column">
                        <div class="box" v-if="chat.user.id === getUser.id">
                            <p>{{ chat.message }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br />
        <form @submit.prevent="sendMessage">
            <div class="columns">
                <div class="column is-four-fifths">
                    <input
                        class="input is-primary"
                        type="text"
                        placeholder="Enter your message"
                        v-model="msg"
                    />
                </div>
                <div class="column">
                    <button
                        class="button is-primary is-fullwidth"
                        type="submit"
                    >
                        Send
                    </button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
    props: ['classroom_id'],
    data() {
        return {
            chatSocket: null,
            msg: null,
            chats: [],
        }
    },
    computed: {
        ...mapGetters(['getUser']),
    },
    mounted() {
        this.connectRoom()
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/chats/classrooms`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => (this.chats = data))
            .catch((e) => console.log(e))
    },
    methods: {
        connectRoom() {
            this.chatSocket = new WebSocket(
                `ws://localhost:8000/ws/chats/classrooms/${this.classroom_id}/`
            )

            this.chatSocket.onmessage = this.receiveMessage
            this.chatSocket.onclose = this.connectionClosed
        },
        sendMessage() {
            this.chatSocket.send(
                JSON.stringify({
                    message: this.msg,
                    user_id: this.getUser.id,
                    classroom_id: this.classroom_id,
                })
            )
            this.msg = null
        },
        connectionClosed(e) {
            console.error('Chat socket closed unexpectedly')
        },
        receiveMessage(e) {
            const data = JSON.parse(e.data)
            this.chats.push(data)
        },
    },
}
</script>

<style>
</style>
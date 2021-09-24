<template>
    <div>
        <h1>Discussion</h1>
        <div class="card">
            <div class="card-body chat-care">
                <ul class="chat">
                    <ChatMessage
                        v-for="chat in chats"
                        :key="chat.id"
                        :chat="chat"
                    />
                </ul>
            </div>
            <div class="card-footer">
                <form @submit.prevent="sendMessage">
                    <div class="input-group">
                        <input
                            id="btn-input"
                            type="text"
                            v-model="msg"
                            class="form-control input-sm"
                            placeholder="Type your message here..."
                        />
                        <span class="input-group-btn">
                            <button
                                class="btn btn-primary"
                                id="btn-chat"
                                type="submit"
                            >
                                Send
                            </button>
                        </span>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import ChatMessage from '@/components/discussions/ChatMessage.vue'

export default {
    name: 'Discussion',
    components: {
        ChatMessage,
    },
    props: ['classroom_id'],
    computed: {
        ...mapGetters(['getUser']),
    },
    data() {
        return {
            chatSocket: null,
            msg: null,
            chats: [],
        }
    },
    methods: {
        connectRoom() {
            this.chatSocket = new WebSocket(
                `${process.env.VUE_APP_WS_URL}/ws/chats/classrooms/${this.classroom_id}/`
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
    mounted() {
        this.connectRoom()
        axios
            .get(`${process.env.VUE_APP_API_URL}/api/chats/classrooms`, {
                params: {
                    classroom_id: this.classroom_id,
                },
            })
            .then(({ data }) => {
                this.chats = data
            })
            .catch((e) => console.log(e))
    },
}
</script>

<style>
.chat {
    list-style: none;
    margin: 0;
    padding: 0;
}

.chat li {
    margin-bottom: 40px;
    padding-bottom: 5px;
    /* border-bottom: 1px dotted #B3A9A9; */
    margin-top: 10px;
    width: 80%;
}

.chat li .chat-body p {
    margin: 0;
    /* color: #777777; */
}

.chat-care {
    overflow-y: scroll;
    height: 650px;
}
.chat-care .chat-img {
    width: 50px;
    height: 50px;
}
.chat-care .img-circle {
    border-radius: 50%;
}
.chat-care .chat-img {
    display: inline-block;
}
.chat-care .chat-body {
    display: inline-block;
    max-width: 80%;
    background-color: #cccccc;
    border-radius: 12.5px;
    padding: 15px;
}
.chat-care .chat-body strong {
    color: #000000;
}

.chat-care .self {
    text-align: right;
    float: right;
}
.chat-care .self p {
    text-align: left;
}
.chat-care .agent {
    text-align: left;
    float: left;
}
.chat-care .left {
    float: left;
}
.chat-care .right {
    float: right;
}

.clearfix {
    clear: both;
}

::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    background-color: #f5f5f5;
}

::-webkit-scrollbar {
    width: 12px;
    background-color: #f5f5f5;
}

::-webkit-scrollbar-thumb {
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    background-color: #555;
}
</style>
<template>
    <div class="container mt-5">
        <form @submit.prevent="handleLogin">
            <div class="mb-3 row">
                <label for="staticEmail" class="col-sm-2 col-form-label"
                    >Email</label
                >
                <div class="col-sm-10">
                    <input
                        type="text"
                        class="form-control"
                        id="staticEmail"
                        v-model="email"
                    />
                </div>
            </div>
            <div class="mb-3 row">
                <label for="inputPassword" class="col-sm-2 col-form-label"
                    >Password</label
                >
                <div class="col-sm-10">
                    <input
                        type="password"
                        class="form-control"
                        id="inputPassword"
                        v-model="password"
                    />
                </div>
            </div>
            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Login',
    components: {},
    data() {
        return {
            email: null,
            password: null,
            error: null,
        }
    },
    methods: {
        handleLogin() {
            this.$store
                .dispatch('login', {
                    email: this.email,
                    password: this.password,
                })
                .then(() => {
                    if (this.$route.query.redirect) {
                        this.$router.push(this.$route.query.redirect)
                    } else {
                        this.$router.push({ name: 'Home' })
                    }
                })
                .catch((err) => (this.error = err.response.data.error))
        },
    },
}
</script>

<style>
</style>
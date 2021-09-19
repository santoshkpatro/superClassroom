<template>
    <div class="box">
        <h3>{{ assignment.title }}</h3>
        <p>Submission On - {{ assignment.submission_on }}</p>
        <br />
        <h1>Submit your assignment</h1>
        <div class="file">
            <label class="file-label">
                <input
                    class="file-input"
                    type="file"
                    name="file"
                    id="file"
                    ref="file"
                    @change="handleUpload"
                />
                <span class="file-cta">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label"> Choose a file… </span>
                </span>
            </label>
            <button @click="submitFile()">Submit</button>
        </div>
    </div>
</template>

<script>
export default {
    props: ['classroom_id', 'assignment'],
    data() {
        return {
            file: '',
        }
    },
    methods: {
        handleUpload() {
            this.file = this.$refs.file.files[0]
        },
        submitFile() {
            // let formData = new FormData()
            // formData.append('file', this.file)

            console.log(submitted)
        },
    },
}
</script>

<style>
</style>
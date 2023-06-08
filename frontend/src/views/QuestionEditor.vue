<template>
    <div class="container my-2">
        <h1 class="mb-3">Ask a Question</h1>
        <form @submit.prevent="onSubmit">
            <textarea v-model="questionBody" class="form-control" placeholder="What do you want to ask?"
                rows="4"></textarea>
            <button type="submit" class="btn btn-outline-primary mt-3">Publish</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>


<script>
import { axios } from "@/common/api.service.js";
export default {
    name: "QuestionEditor",
    props: {
        slug: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            questionBody: null,
            error: null
        }
    },
    methods: {
        async performNetworkRequest() {
            let endpoint = "/api/v1/questions/";
            let method = "POST";
            if (this.slug !== undefined && this.slug !== "") {
                endpoint += `${this.slug}/`;
                method = "PUT";
            }
            try {
                const response = await axios({
                    method: method,
                    url: endpoint,
                    data: { content: this.questionBody }
                })
                this.$router.push({ name: 'question', params: { slug: response.data.slug } })
            } catch (error) {
                this.error = error.response.statusText;
            }
        },
        onSubmit() {
            if (!this.questionBody) {
                this.error = "You can't send an empty question!";
            } else if (this.questionBody.length > 240) {
                this.error = "Ensure this field has no more than 240 characters!";
            } else {
                this.performNetworkRequest();
            }
        }
    },
    created() {
        document.title = "Editor - ThinkAsk";
    },
    async beforeRouteEnter(to, from, next) {
        if (to.params.slug !== undefined && to.params.slug !== "") {
            const endpoint = `/api/v1/questions/${to.params.slug}/`;
            try {
                const response = await axios.get(endpoint);
                return next(vm => vm.questionBody = response.data.content)
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        }
        else {
            return next();
        }

    }
};
</script>
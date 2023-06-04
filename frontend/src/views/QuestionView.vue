<template>
    <div class="container mt-3">
        <div v-if="question">
            <h1>{{ question.content }}</h1>
            <p class="mb-0">Posted by: <span class="author-name">{{ question.author }}</span></p>
            <p>{{ question.created_at }}</p>
        </div>
        <div v-else>
            <h1 class="error text-center">404 - Question Not Found</h1>
        </div>
    </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
export default {
    name: "QuestionView",
    props: {
        slug: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            question: null
        }
    },
    methods: {
        setPageTitle(title){
            document.title = title;
        },
        async getQuestionData() {
            const endpoint = `/api/v1/questions/${this.slug}/`;
            try {
                const response = await axios.get(endpoint);
                this.question = response.data;
                this.setPageTitle(response.data.content);
            } catch (error) {
                console.log(error.response);
                const title = "404 - not Found!"
                this.setPageTitle(title);
            }
        }
    },
    created() {
        this.getQuestionData();
    }
};
</script>

<style>
.author-name {
    font-weight: bold;
    color: #0d6efd;
}

.error {
    color: #dc3545;
}
</style>
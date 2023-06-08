<template>
    <div>
        <p class="text-muted">
            <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
        </p>
        <p class="white-space: pre-wrap;">{{ answer.body }}</p>
        <div v-if="isAnswerAuthor">
            <router-link :to="{ name: 'answer-editor', params: { uuid: answer.uuid } }" class="btn btn-sm btn-secondary">
                Edit
            </router-link>
            <button class="btn btn-sm btn-danger mx-1" @click="showDeleteConfirmationBtn = !showDeleteConfirmationBtn">
                Delete
            </button>
            <button v-show="showDeleteConfirmationBtn" class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">
                Yes, delete my Answer
            </button>
        </div>
        <hr>
    </div>
</template>


<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true,
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    data(){
        return {
            showDeleteConfirmationBtn: false
        }
    },
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        triggerDeleteAnswer(){
            this.$emit("delete-answer", this.answer);
        }
    }
};
</script>


<style></style>
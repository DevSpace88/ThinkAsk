<template>
    <div>
        <p class="text-muted">
            <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
        </p>
        <p class="white-space: pre-wrap;">{{ answer.body }}</p>
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
        }
    }
};
</script>


<style>
</style>
<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link class="navbar-brand" :to="{ name: 'home' }">ThinkAsk</router-link>
           
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto">

                    <li class="nav-item">
                        <router-link class="btn btn-outline-primary" :to="{ name: 'question-editor' }">Ask Question</router-link>
                   
                    </li>

                    <li class="nav-item mx-3">
                    <a class="btn btn-outline-primary" href="/accounts/logout/">Log out</a>
                    </li>
                    
                </ul>
               
            </div>
        </div>
    </nav>
</template>

<script>
// import HomeView from '@/views/HomeView.vue';

export default {
    name: "NavbarComponent",
}
</script>

<style>
.my-navbar {
    border-bottom: 1px solid #dddddd;
}

.navbar-brand {
    font-weight: bold;
    font-size: 150%;
    border-color: #0d6efd;
}

.navbar-brand:hover {
    color: #0d6efd !important;
    border-color: #0d6efd;
}

</style>


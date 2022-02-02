<template>
    <div>
        <span class="bg"></span>
        <v-card outlined color="transparent">
            <v-card-title class="justify-center">
                <div class="text-title text-md-h1 title-color">Projects</div>
            </v-card-title>
        </v-card>
        <v-card outlined color="transparent">
            <div class="text-center text-md-h5 title-color font-weight-light">
                See all my projects at:
                <a href="https://github.com/LeonPatmore">
                    https://github.com/LeonPatmore
                </a>
            </div>
        </v-card>
        <v-card
            v-for="project in projects"
            v-bind:key="project.name"
            class="pa-2 ma-10"
            color="transparent"
            hover
            rounded
        >
            <a
                :href="project.repo"
                target="_blank"
                style="text-decoration: none"
            >
                <v-card-title class="pa-1 white--text">{{
                    project.name
                }}</v-card-title>
                <v-card-text class="pa-1 white--text font-weight-light">{{
                    project.desc
                }}</v-card-text>
                <v-card-text class="pa-1 white--text font-weight-light">{{
                    project.repo
                }}</v-card-text>
            </a>
        </v-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
            projects: [
                {
                    name: 'Personal Website',
                    desc: 'My personal VueJS website that you are viewing now!',
                    repo: 'https://github.com/LeonPatmore/leon-patmore-website',
                },
                {
                    name: 'Shopping Predictor',
                    desc: 'A Python AWS Lambda with functions to make my life easier! Uses AWS SAM.',
                    repo: 'https://github.com/LeonPatmore/life-efficiency',
                },
            ],
        };
    },
};
</script>

<style scoped>
a {
    color: inherit;
}
.title-color {
    color: rgb(255, 255, 255, 0.85);
}
.bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background: url('https://cdn.pixabay.com/photo/2016/03/26/13/09/organic-1280537_1280.jpg')
        no-repeat center center;
    background-size: cover;
    background-color: transparent;
    transform: scale(1.1);
}
</style>

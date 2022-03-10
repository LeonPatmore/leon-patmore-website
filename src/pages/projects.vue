<template>
    <div>
        <span class="bg"></span>
        <v-container>
            <v-card outlined color="transparent">
                <v-card-title class="justify-center">
                    <div class="text-md-h1 title-color text-h3">Projects</div>
                </v-card-title>
            </v-card>
            <v-card outlined color="transparent">
                <div
                    class="text-center text-md-h5 title-color font-weight-light"
                >
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
                <div class="d-flex flex-no-wrap justify-space-between">
                    <a
                        :href="project.repo"
                        target="_blank"
                        style="text-decoration: none"
                    >
                        <v-card-title
                            class="pa-1 black--text text-wrap"
                            style="word-break: keep-all"
                            >{{ project.name }}</v-card-title
                        >
                        <v-card-text
                            class="pa-1 black--text font-weight-light"
                            >{{ project.desc }}</v-card-text
                        >
                        <v-card-text
                            class="pa-1 black--text font-weight-light text-caption hidden-sm-and-down"
                            >{{ project.repo }}</v-card-text
                        >
                    </a>
                    <v-img
                        class="ma-1"
                        min-width="25"
                        width="2vh"
                        max-width="150"
                    >
                        <v-img :src="project.lang"></v-img>
                    </v-img>
                </div>
            </v-card>
        </v-container>
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
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/vuejs.png',
                },
                {
                    name: 'Shopping Predictor',
                    desc: 'A Python AWS Lambda with functions to make my life easier! Uses AWS SAM.',
                    repo: 'https://github.com/LeonPatmore/life-efficiency',
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/python.png',
                },
                {
                    name: 'Behave Healthchecks',
                    desc: 'A plugin for Behave, which automatically sends healthcheck io updates.',
                    repo: 'https://github.com/LeonPatmore/behave-healthchecks',
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/python.png',
                },
                {
                    name: 'Mongo Rest API',
                    desc: 'A REST API for MongoDB written in kotlin.',
                    repo: 'https://github.com/LeonPatmore/document-reader',
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/kotlin.png',
                },
                {
                    name: 'Spammer',
                    desc: 'A performance testing tool written in NodeJS.',
                    repo: 'https://github.com/LeonPatmore/spammer-v2',
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/nodeJs.png',
                },
                {
                    name: 'Messages API Websocket',
                    desc: 'Websocket integration for a messaging API with AWS Api Gateway integration.',
                    repo: 'https://github.com/LeonPatmore/messages-api-websocket',
                    lang: 'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/nodeJs.png',
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
    color: rgb(0, 0, 0, 0.85);
}
.bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background: url('~@/static/mountain.jpg') no-repeat center center;
    background-size: cover;
    background-color: transparent;
    transform: scale(1.1);
}
</style>

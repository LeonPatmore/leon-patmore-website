<template>
    <div>
        <span class="bg"></span>
        <v-container>
            <v-row class="no-gutters">
                <v-col cols="12">
                    <v-card outlined color="transparent">
                        <v-card-title class="justify-center">
                            <div
                                class="text-sm-h2 text-md-h1 title-color mt-10 text-h4"
                            >
                                Leon Patmore
                            </div>
                        </v-card-title>
                    </v-card>
                </v-col>
            </v-row>
            <v-row class="no-gutters pb-md-8">
                <v-col cols="12">
                    <v-card outlined color="transparent">
                        <v-card-text
                            class="text-center text-subtitle-1 black--text"
                            >Hello and welcome to my website! Please find my CV
                            and projects on the other pages.</v-card-text
                        >
                    </v-card>
                </v-col>
            </v-row>
            <v-row class="justify-center no-gutters pb-md-8">
                <v-col :lg="8" :md="10" cols="12">
                    <v-card class="pa-5 pt-0" color="rgb(0, 0, 0, 0.0)">
                        <v-img
                            max-width="1000px"
                            src="https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/my_website.png"
                        />
                    </v-card>
                </v-col>
            </v-row>
            <v-row class="no-gutters">
                <v-col
                    v-for="img in images"
                    v-bind:key="img"
                    class="d-flex justify-center align-center"
                >
                    <v-img
                        class="ma-1"
                        min-width="70"
                        width="6vh"
                        max-width="150"
                        :src="img"
                    ></v-img>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    data() {
        return {
            images: [
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/awsCertifiedDeveloper.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/helm.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/java.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/k8.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/python.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/spring.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/nodeJs.png',
                'https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/kotlin.png',
            ],
        };
    },
};
</script>

<style>
.title-color {
    color: rgb(0, 0, 0, 0.65);
}
.bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background: url('~@/static/walkingOverRiver.jpg') no-repeat center center;
    background-size: cover;
    background-color: transparent;
    transform: scale(1.1);
    opacity: 0.8;
}
</style>

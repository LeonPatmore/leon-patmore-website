<template>
    <div>
        <span class="bg"></span>
        <v-card outlined color="transparent">
            <v-card-title class="justify-center">
                <div class="text-title text-md-h1 title-color">Projects</div>
            </v-card-title>
        </v-card>
        <v-card outlined color="transparent">
            <v-card-text
                class="text-center text-md-h5 white--text font-weight-light"
            >
                See all my projects at:
                <a href="https://github.com/LeonPatmore">
                    https://github.com/LeonPatmore
                </a>
            </v-card-text>
        </v-card>
        <v-card class="pa-2 ma-10" outlined color="transparent">
            <b-card-text class="white--text font-weight-light">
                Hello there!
            </b-card-text>
        </v-card>
    </div>
</template>

<style scoped>
a {
    color: inherit;
}
.title-color {
    color: rgb(255, 255, 255, 0.8);
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

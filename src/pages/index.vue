<template>
    <div>
        <span class="bg"></span>
        <v-card outlined color="transparent">
            <v-card-title class="justify-center">
                <div class="text-md-h1 title-color mt-10 text-h3">
                    Leon Patmore
                </div>
            </v-card-title>
        </v-card>
        <v-row justify="center">
            <v-col cols="12">
                <v-card
                    outlined
                    color="transparent"
                    class="pa-5 ma-4 mb-1 mt-1 pt-0"
                >
                    <v-card-text class="text-center text-subtitle-1 black--text"
                        >Hello and welcome to my website! Please find my CV and
                        projects on the other pages.</v-card-text
                    >
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-card
                    outlined
                    color="transparent"
                    class="pa-5 ma-4 mb-1 mt-1"
                    align="center"
                >
                    <v-img
                        max-width="100"
                        contain
                        src="/awsCertifiedDeveloper.png"
                    ></v-img>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

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

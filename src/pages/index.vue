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
        <v-card
            class="d-flex align-center pa-10 ma-4"
            outlined
            color="transparent"
        >
            <v-card-text>Hello and welcome to my website!</v-card-text>
        </v-card>
    </div>
</template>

<style>
.title-color {
    color: rgb(0, 0, 0, 0.75);
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

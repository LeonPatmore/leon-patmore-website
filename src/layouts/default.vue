<template>
    <v-app>
        <v-navigation-drawer
            dark
            v-model="drawer"
            absolute
            temporary
            color="grey darken-1"
        >
            <v-list rounded>
                <v-list-item to="/" nuxt-link>
                    <v-list-item-icon>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>Home</v-list-item-content>
                </v-list-item>
                <v-list-item to="/projects" nuxt-link>
                    <v-list-item-icon>
                        <v-icon>mdi-source-repository-multiple</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>Projects</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item
                    href="https://leon-patmore-cv.s3.eu-west-2.amazonaws.com/CV-Developer.pdf"
                >
                    <v-list-item-icon>
                        <v-icon>mdi-file-document</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>CV</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar
            app
            dark
            absolute
            color="grey darken-1"
            elevation="10"
            shaped
        >
            <v-app-bar-nav-icon
                dark
                @click.stop="drawer = !drawer"
            ></v-app-bar-nav-icon>
            <v-toolbar-title>Leon Patmore</v-toolbar-title>
        </v-app-bar>
        <v-main>
            <nuxt />
        </v-main>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            drawer: false,
        };
    },
};
</script>

module.exports = {
    telemetry: false,
    srcDir: 'src/',
    head: {
        title: 'leon-patmore-website',
        htmlAttrs: {
            lang: 'en',
        },
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' },
        ],
        link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
    css: [],
    plugins: [],
    components: true,
    buildModules: ['@nuxtjs/vuetify'],
    modules: ['bootstrap-vue/nuxt'],
    build: {},
};

FROM node:14
RUN npm install -g serverless-domain-manager
RUN npm install -g serverless-offline
RUN npm install -g serverless

WORKDIR /app

COPY package.json package.json
RUN npm install --only=prod

COPY .nuxt .nuxt
COPY handler.js handler.js
COPY nuxtBuild.js nuxtBuild.js
COPY binaryMimeTypes.js binaryMimeTypes.js
COPY nuxt.config.js nuxt.config.js
COPY .env .env
COPY serverless.yaml serverless.yaml

RUN serverless package --package /app/package

ENTRYPOINT ["tail", "-f", "/dev/null"]

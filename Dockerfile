FROM node:14
RUN npm install -g serverless-domain-manager
RUN npm install -g serverless-offline

WORKDIR /app

COPY package.json package.json
RUN npm install --only=prod

COPY .nuxt/dist/** .nuxt/dist
COPY handler.js handler.js
COPY nuxtBuild.js nuxtBuild.js
COPY binaryMimeTypes.js binaryMimeTypes.js
COPY .env .env
COPY serverless.yaml serverless.yaml

RUN npx sls deploy

ENTRYPOINT ["tail", "-f", "/dev/null"]

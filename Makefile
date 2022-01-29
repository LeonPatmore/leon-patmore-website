help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test:
	npm test

fmt:
	npx prettier -c "**"

build:
	npm run build

run: build
	npm start

dev:
	npx nuxt

local: build
	npx sls offline start

push: build
	npx sls deploy

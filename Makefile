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

deploy:
	npx sls deploy --package ./package

package:
	docker build -t web-package .
	docker run --name web-package -d web-package
	docker cp web-package:/app/package ./package
	docker rm -f web-package

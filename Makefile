help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test:
	npm test

fmt:
	npx prettier -c "**"

test:
	npm test

build:
	npm run build

run: build
	npm start

dev:
	npx nuxt

clean:
	rm ./package

local: build
	npx sls offline start

package:
	npx serverless package --package ./package

docker-package:
	docker build -t web-package .
	docker run --name web-package -d web-package
	docker cp web-package:/app/package ./package
	docker rm -f web-package

deploy:
	npx serverless deploy --package ./package

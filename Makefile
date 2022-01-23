help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test:
	npm test

fmt:
	npx prettier -c "**"

run:
	npm start

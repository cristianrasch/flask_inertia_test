MAKEFLAGS+="-j 2"

init:
	poetry install
	cd "static/vue" && npm install

dev-python:
	poetry run flask run

dev-js:
	npm run --prefix "static/vue" build:dev

dev: dev-python dev-js

MAKEFLAGS+="-j 2"

init:
	poetry install
	cp .env.example .env
	cd static/vue && npm install

dev-python:
	poetry run flask run

dev-js:
	npm run --prefix static/vue build:dev

dev: dev-python dev-js

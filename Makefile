MAKEFLAGS+="-j 2"

FLASK_DEV=FLASK_APP="app.app:create_app('dev')" FLASK_ENV=development

init:
	pip install -r requirements.txt
	cd "static/vue" && npm install

dev-python:
	$(FLASK_DEV) flask run

dev-js:
	@npm run --prefix "static/vue" build:dev

dev: dev-python dev-js

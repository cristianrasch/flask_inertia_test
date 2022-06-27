import os
from pathlib import Path

from flask import Flask, flash, get_flashed_messages

from .ext import flask_static_digest, inertia
from .settings import CONFIG
from .blueprints.main import main_bp
from .csrf import check_csrf_token, set_csrf_cookie

ROOT_DIR = Path(__file__).resolve().parent.parent
FLASK_ENV = os.getenv("FLASK_ENV", "production")


def create_app(config_name=FLASK_ENV):
    app = Flask(
        __name__,
        template_folder=ROOT_DIR / "templates",
        static_folder=ROOT_DIR / "static" / "dist",
    )
    app.config.from_object(CONFIG[config_name])

    flask_static_digest.init_app(app)

    # init inertia
    inertia.init_app(app)
    inertia.share(
        "flash_success", lambda: get_flashed_messages(category_filter="success")
    )
    inertia.share("flash_error", lambda: get_flashed_messages(category_filter="error"))

    # blueprints
    app.register_blueprint(main_bp)

    # CSRF protection
    app.before_request(check_csrf_token)
    app.after_request(set_csrf_cookie)

    return app

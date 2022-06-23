import secrets
import string
import time
from pathlib import Path

from flask import Flask, flash, get_flashed_messages, make_response, redirect, request, session, url_for
from flask_inertia import Inertia, render_inertia


ROOT_DIR = Path(__file__).resolve().parent.parent
CSRF_TOKEN_LENGTH = 25
ALPHABET = string.ascii_letters + string.digits
# ALPHABET = string.ascii_letters + string.digits + string.punctuation


def _check_csrf_token():
    if request.method == "GET":
        return

    req_csrf_token = request.headers.get("X-XSRF-TOKEN", "")
    session_csrf_token = session.pop("csrf_token", "")
    if req_csrf_token != session_csrf_token:
        flash(f"Invalid CSRF token: '{req_csrf_token}'"
              f", expected: '{session_csrf_token}'",
              "error")
        return redirect(request.headers.get("Referer", url_for("index")))
        # return make_response(f"Invalid CSRF token: '{req_csrf_token}'"
        #                      f", expected: '{session_csrf_token}'",
        #                      403)


def _gen_csrf_token():
    return ''.join(secrets.choice(ALPHABET) for i in range(CSRF_TOKEN_LENGTH))


def _set_csrf_cookie(response):
    csrf_token = _gen_csrf_token()
    response.set_cookie("XSRF-TOKEN", csrf_token)
    session["csrf_token"] = csrf_token

    return response


def index():
    return render_inertia("Index")


def about():
    return render_inertia("StaticPage", {'msg': 'About Us'})


def contact():
    errors = {}

    if request.method == "POST":
        time.sleep(1)
        form = request.get_json() if request.is_json else request.form
        name = form.get("name", "").strip()
        if not name:
            errors["name"] = "Name is required."
        if not form.get("email", "").strip():
            errors["email"] = "Email is required."
        if not form.get("subject", "").strip():
            errors["subject"] = "Subject is required."

        if errors:
            flash("Please correct the error(s) below", "error")
        else:
            flash(f"Thank you for your message '{name}'", "success")
            return redirect(url_for("contact"))

    return render_inertia("Contact", {'msg': 'Contact Us', 'errors': errors})


def create_app(config_filename: str) -> Flask:
    app = Flask(
        __name__,
        template_folder=ROOT_DIR / "templates",
        static_folder=ROOT_DIR / "static" / "dist",
    )
    app.config.from_pyfile(f"{config_filename}.py")
    inertia = Inertia(app)
    inertia.share("flash_success", lambda: get_flashed_messages(category_filter="success"))
    inertia.share("flash_error", lambda: get_flashed_messages(category_filter="error"))

    app.add_url_rule("/", "index", index)
    app.add_url_rule("/about_us", "about", about)
    app.add_url_rule("/contact_us", "contact", contact, methods=["GET", "POST"])
    app.before_request(_check_csrf_token)
    app.after_request(_set_csrf_cookie)

    return app

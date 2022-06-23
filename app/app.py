import time
from pathlib import Path

from flask import Flask, flash, get_flashed_messages, redirect, request, url_for
from flask_inertia import Inertia, render_inertia


ROOT_DIR = Path(__file__).resolve().parent.parent


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
            flash("Please correct the error(s) below", "alert")
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
    inertia.share("title", "Welcome to my app!")
    inertia.share("success", lambda: get_flashed_messages(category_filter="success"))
    inertia.share("alert", lambda: get_flashed_messages(category_filter="alert"))

    app.add_url_rule("/", "index", index)
    app.add_url_rule("/about_us", "about", about)
    app.add_url_rule("/contact_us", "contact", contact, methods=["GET", "POST"])

    return app

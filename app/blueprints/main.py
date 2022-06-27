import time

from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
)
from flask_inertia import render_inertia


main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    return render_inertia("Index")


@main_bp.get("/about")
def about():
    return render_inertia("StaticPage", {"msg": "About Us"})


@main_bp.route("/contact", methods=["GET", "POST"])
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
            return redirect(url_for(".contact"))

    return render_inertia("Contact", {"msg": "Contact Us", "errors": errors})

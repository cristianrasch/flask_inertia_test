import secrets
import string

from flask import flash, request, session, redirect, url_for

CSRF_TOKEN_LENGTH = 25
ALPHABET = string.ascii_letters + string.digits


def check_csrf_token():
    if request.method == "GET":
        return

    req_csrf_token = request.headers.get("X-XSRF-TOKEN", "")
    session_csrf_token = session.pop("csrf_token", "")
    if req_csrf_token != session_csrf_token:
        flash(
            f"Invalid CSRF token: '{req_csrf_token}'"
            f", expected: '{session_csrf_token}'",
            "error",
        )
        return redirect(request.headers.get("Referer", url_for("index")))


def _gen_csrf_token():
    return "".join(secrets.choice(ALPHABET) for i in range(CSRF_TOKEN_LENGTH))


def set_csrf_cookie(response):
    csrf_token = _gen_csrf_token()
    response.set_cookie("XSRF-TOKEN", csrf_token)
    session["csrf_token"] = csrf_token

    return response

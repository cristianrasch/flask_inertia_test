from flask import current_app, url_for

from ..ext import flask_static_digest


def asset_url_for(endpoint, **values):
    env = current_app.config.get("ENV")
    if env == "production" and not current_app.config.get("TESTING"):
        return flask_static_digest.static_url_for(endpoint, **values)
    else:
        return url_for(endpoint, **values)


def asset_processors():
    return dict(
        asset_url_for=asset_url_for,
    )

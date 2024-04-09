#!/usr/bin/env python3

"""
A route in oython flask
Import and configure flask babel
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    A class defining a basic
    babel configurations
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    A function that gets the best match for
    user locale.
    """
    # Checks the 'locale' parameter is present in the request URL
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"])
def render_index():
    """
    A function that renders the html
    template index.html
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

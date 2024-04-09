#!/usr/bin/env python3

"""
modules to create a route in flask
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
     Functions that provides basic Babel configurations
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
     function to get best match for user locale.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"])
def render_index():
    """
    Render the html template index.html index.html
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

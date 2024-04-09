#!/usr/bin/env python3
"""
A module using flask, configue flask babel
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Basic Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Returns the best match for user locale"""
    return (request.accept_languages.best_match(app.config["LANGUAGES"]))


@app.route('/')
def get_index() -> str:
    """Renders the html index page index.html"""
    return (render_template('2-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

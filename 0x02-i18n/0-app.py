#!/usr/bin/env python3
"""
basic flask app that renders from index.html
"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def get_index() -> str:
    """Function index.html template that simply outputs
    “Welcome to Holberton” as page title """
    return (render_template('0-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

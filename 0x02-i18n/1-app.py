#!/usr/bin/env python3
"""Basic Flask app task 1"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
     list of languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configuring the app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
     `index.html`
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

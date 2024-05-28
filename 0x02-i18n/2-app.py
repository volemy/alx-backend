#!/usr/bin/env python3
"""Get locale from request 2-app.py"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    returns the rendered template `index.html`
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

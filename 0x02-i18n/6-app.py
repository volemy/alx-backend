#!/usr/bin/env python3
"""Task 6-app.py
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """
    Returning
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configuring the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """
    returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Returns local
    user_locale = None
    if g.user:
        user_locale = g.user.get('locale')
    locale = request.args.get('locale') or user_locale
    if locale in app.config['LANGUAGES']:
        return locale
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """mocking log in
    """
    return render_template('6-index.html', users=users)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)

#!/usr/bin/env python3
"""Basic Flask app 0-app.py"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    The function `index()` returns the rendered template `index.html`
    :return: The index.html file is being returned.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

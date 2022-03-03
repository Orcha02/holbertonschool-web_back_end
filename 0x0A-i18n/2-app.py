#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Babel config class """
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = 'en'
    Babel.default_timezone = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    """ Returns index """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host=host, port=port)

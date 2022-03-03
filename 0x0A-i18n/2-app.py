#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config Class."""
    LANGUAGES = ['en', 'fr']
    Babel.default_locale = 'en'
    Babel.default_timezone = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    """Render index.html."""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

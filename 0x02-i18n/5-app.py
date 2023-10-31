#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
    },
}


@app.before_request
def before_request():
    user_id = request.args.get('login_as', type=int, default=None)
    g.user = get_user(user_id)


def get_user(user_id):
    return users.get(user_id)


@app.route('/')
def index():
    if g.user:
        return render_template('5-index.html', user=g.user)
    else:
        return render_template('5-index.html', user=None)


if __name__ == '__main__':
    app.run()

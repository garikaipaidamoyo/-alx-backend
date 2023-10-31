#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    if 'locale' in request.args and request.args['locale'] in app.config[
            'LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone', type=str, default=None)
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return request.user.timezone if hasattr(
        request.user, 'timezone') else app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()

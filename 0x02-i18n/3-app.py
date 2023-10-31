#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
babel.init_app(app, default='en', default_timezone='UTC')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()

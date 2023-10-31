#!/usr/bin/env python3

from flask import Flask, render_template
from babel import Babel, format_datetime
import pytz
import datetime

app = Flask(__name__)
babel = Babel(app)


@babel.timezoneselector
def get_timezone():
    # Your logic to infer the time zone, e.g.,
    # from URL parameters or user settings.
    return user_timezone  # Replace with your actual logic.


@app.route('/')
def home():
    # Get the current time in the inferred time zone.
    current_time = format_datetime(
        datetime.datetime.now(pytz.timezone(get_timezone())))
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run()

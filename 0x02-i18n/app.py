#!/usr/bin/env python3
""" module to basic setup of flask """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ class to create configuraton languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """ determine best match with language """
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    request_header = request.headers.get('locale')
    if request_header and request_header in app.config['LANGUAGES']:
        return request_header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ determine time zone """
    request_timezone = request.args.get('timezone')
    if request_timezone:
        try:
            return pytz.timezone(request_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                return pytz.timezone(timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@app.route('/')
def get_template():
    """ function that render route '/' and it's template """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()

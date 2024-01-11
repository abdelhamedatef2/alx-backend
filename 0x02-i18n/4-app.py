#!/usr/bin/env python3
""" module to basic setup of flask """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ class to create configuraton languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ determine best match with language """
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_template():
    """ function that render route '/' and it's template """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()

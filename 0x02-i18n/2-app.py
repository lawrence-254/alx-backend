#!/usr/bin/env python3
'''
a basic Flask app
'''
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    '''
    configures babel languages
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''
    fetches for locale of the user
    '''
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def index() -> str:
    '''
    route for index.html
    '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

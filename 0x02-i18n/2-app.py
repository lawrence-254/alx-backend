#!/usr/bin/env python3
'''
a basic Flask app
'''
from flask_babel import Babel
from flask import Flask, render_template


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


@app.route('/')
def index() -> str:
    '''
    route for index.html
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

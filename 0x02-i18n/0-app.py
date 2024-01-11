#!/usr/bin/env python3
""" module to basic setup of flask """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_template():
    """ function that render route '/' and it's template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

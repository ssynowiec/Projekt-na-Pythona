# TODO: This file needs major changes but at least it works

from src import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

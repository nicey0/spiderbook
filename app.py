#-Imports--------------------------------------------------#
import os

from flask import Flask, request, redirect, make_response, render_template, url_for
from flask_script import Manager
from api import *

#-Flask-App-Setup------------------------------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET']

#-View-Functions-------------------------------------------#
@app.route('/')
def index():
    return "<p>Index</p>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    # request.form
    return "<p>Register Page</p>"

@app.route('/post/create')
def create_post():
    data = {
        "title": "Post",
        "body": "Hello, world!",
        "img": None
    }
    print(API_create_post(data)['code'])
    return '<p>Post created!</p>'

#-Running-the-server---------------------------------------#
if __name__ == '__main__':
    app.run (
        host="localhost",
        port=8000,
        debug=True
    )

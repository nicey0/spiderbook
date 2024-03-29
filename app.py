#-Imports--------------------------------------------------#
import os, time

from flask import Flask, request, redirect, make_response, render_template, url_for
from flask_script import Manager
from api import *

#-Flask-App-Setup------------------------------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET']

def write_file(bcontent):
    with open('hello.jpg', 'wb') as file:
        file.write(bcontent)

#-View-Functions-------------------------------------------#
'''
Notes:
Get form data: request.form
Get URI arguments: request.args.get('ARGUMENT_NAME')
Get POST body JSON: request.data
'''
@app.route('/')
def index():
    return "<p>Index</p>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    # request.form
    return "<p>Register Page</p>"

@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        data = dict(request.form)
        image = request.files.get('img')
        imageURL = 'images/'+image.filename
        image.save(imageURL)

        if not data.get('body'): data['body'] = None
        if not image: data['img_url'] = None

        data['img_url'] = imageURL
        data['author'] = 'Anon'

        code = API_create_post(data)['code']
        if code == 'success!':
            return '<h2>Post created!</h2>'
        else:
            return f'<h2>Error: {code}</h2>'
    return render_template('create_post.html')

#-Running-the-server---------------------------------------#
if __name__ == '__main__':
    app.run (
        host="localhost",
        port=8000,
        debug=True
    )

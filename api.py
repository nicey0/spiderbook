#-Imports--------------------------------------------------#
import os

from flask import Flask, request, redirect, make_response, render_template, url_for, jsonify
from flask_script import Manager

from API.db_management import create_post, get_posts

#-Flask-setup----------------------------------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET']

#-View-functions-------------------------------------------#
@app.route('/a', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(request.args)
        print('Method: GET')
    else:
        print(request.data)
        print('Method: POST')
    return jsonify("a")

#-Running-the-server---------------------------------------#
if __name__ == '__main__':
    app.run (
        host="localhost",
        port=5000,
        debug=True
    )

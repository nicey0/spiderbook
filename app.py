#-Imports--------------------------------------------------#
import os

from flask import Flask, request, redirect, make_response, render_template, url_for
from flask_script import Manager
import api

#-Functions------------------------------------------------#\
def removeLast(s):
    sl = list(s)
    sl.pop()
    return ''.join(sl)

def APIcall(payload, path, method='get'):
    if method.lower() == "get":
        uri = "http://localhost:5000" + path + '?'
        for (k,v) in payload.items(): uri += str(k)+'='+str(v)+'&'
        uri = removeLast(uri)
        print(f"GET {uri}")
        response = requests.get(uri)
    else:
        uri = "http://localhost:5000" + path
        print(f"POST {uri} PAYLOAD: {payload}")
        response = requests.post(uri, json=payload)
    return response

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

#-Running-the-server---------------------------------------#
if __name__ == '__main__':
    app.run (
        host="localhost",
        port=8000,
        debug=True
    )

import flask
from flask import Flask, redirect, render_template, request, url_for

import getDocumentContents
import user
#import saveUserUploads

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/output')
def output():   #removed a name parameter that was throwing type error, do not know its purpose
    return render_template('output.html')

@app.route('/success')
def success():
    return render_template('output.html')

"""Commenting out to test other features

@app.route('/login', methods=['GET', 'POST'])   # Work in progress, adding for visibility
def login():
    if request.method == 'POST':
        # Validate user credentials (e.g., check username and password)

        user_id = 'user123'
        user = user.User(user_id)
        user.login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')
"""

if __name__ == '__main__':
    app.run(debug=True)

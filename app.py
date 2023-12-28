import flask
from flask import Flask, redirect, render_template, request, url_for

import getDocumentContents
import user
#import saveUserUploads

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/output')
def output(name):
    return render_template('output.html')

@app.route('/upload', methods=['POST'])
def upload_files():

    files = request.files.getlist('files')

    for file in files:
        if file.filename == '':
            return "No uploaded files"
        # Handle file upload logic here (e.g., save or process each file)
        files.save(f"/Users/madisonkarcesky/Desktop/{file.filename}")
        getDocumentContents.manipulate_uploaded_file(files)
        return redirect('/success')

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

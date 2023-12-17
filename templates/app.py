import flask
from flask import Flask, redirect, render_template, request, url_for

import getDocumentContents
import saveUserUploads

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

@app.route('/upload.html', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')

    for file in files:
        if file.filename == '':
            continue
        # Handle file upload logic here (e.g., save or process each file)
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)

import flask
from flask import Flask, render_template

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

@app.route('/html')
def html_example():
    return '<h1>This is an HTML response</h1>'

if __name__ == '__main__':
    app.run(debug=True)

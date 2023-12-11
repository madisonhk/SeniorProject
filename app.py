import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is a simple Flask web application.'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/html')
def html_example():
    return '<h1>This is an HTML response</h1>'

@app.route('/template')
def template_example():
    # Assuming you have a 'template.html' file in a 'templates' folder
    return render_template('index.html', message='Flask is awesome!')

if __name__ == '__main__':
    app.run(debug=True)

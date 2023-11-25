from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    uploaded_file = request.files['uploaded_file']

    # Save the file to a specific directory
    upload_folder = 'C:\Projects\Senior Project\UploadedFiles'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, uploaded_file.filename)
    uploaded_file.save(file_path)

    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)

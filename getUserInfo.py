# Calculating the new document that will come from the 

#import to read the document
#import PyPDF2
import os

#Put the content of all the files uploaded into an array
content = []

#Save the info from the doc into a variable of some kind 
def manipulate_uploaded_file(file_path):
    # Add your manipulation code here
    # For example, read the content of the file
    with open(file_path, 'r') as file:
        content.append(file.read())
        print(f"Content of the uploaded file:\n{content}")

if __name__ == '__main__':
    # Assuming you have the file path saved from the upload process
    uploaded_file_path = 'C:\Projects\Senior Project\UploadedFiles/uploaded_file.txt'
    manipulate_uploaded_file(uploaded_file_path)







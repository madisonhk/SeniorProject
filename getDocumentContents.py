# Calculating the new document that will come from the 

#import to read the document
import saveUserUploads
#remove PyPDF2
import os

#Put the content of all the files uploaded into an array
content = []

#Save the info from the doc into a variable of some kind 
def manipulate_uploaded_file(file):
    # Add your manipulation code here
    # For example, read the content of the file
    content.append(file.read())
    print(f"Content of the uploaded file:\n{content}")
    








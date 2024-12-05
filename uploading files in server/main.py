import os
from flask import Flask, request
app=Flask(__name__)
UPLOAD_FOLDER="uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
@app.route('/')
def upload_form():
    return """
<!DOCTYPE html>
<title>upload a file</title>
<h1>upload a file</h1>
<form action="/upload" method="POST" enctype="multipart/form-data">
<input type="file" name="file">
<button type="submit">upload</button></form>
"""
@app.route('/upload',methods=['POST'])
def upolad_file():
    if "file" not in request.files:
        return "no file part in the request"
    file=request.files['file']
    if file.filename=="":
        return "no selective file"
    if file :
        filepath =os.path.join(app.config["UPLOAD_FOLDER"],file.filename)
        file.save(filepath)
        return f"file successfully upload to {filepath}"
if __name__=="__main__":
    app.run (debug=True)
from flask import Flask,request,redirect,url_for
app=Flask(__name__)
votes ={'team A':0,'team B':0}
@app.route('/')
def index():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>pick the winner</title>
</head>
<body>
<h1>pick the winner</h1>
<form method="POST" action='/vote'>
<label>
<input type='radio' name='choice' value='team A' required>team A 
</label><br>
<label>
<input type='radio' name='choice' value='team B' required>team B
</label><br><br>
<button type='submit'>vote</button>
</form>
"""
           

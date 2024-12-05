from flask import Flask,request,render_template_string,jsonify,session
from flask_mail import Mail, message
import random 
app=Flask(__name__)
app.secret_key="Palak725*"
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False
app.config["MAIL_USERNAME"]="palaksrivastava725@gmail.com"
app.config["MAIL_PASSWORD"]="Palak725*"
mail=Mail(app)
otp_form_template="""
<!DOCTYPE html>
<html>
<head>
<title>
Verify Email</title>
</head>
<body>
<h1>Verify your Email</h1>
<form action="/send_otp" method="POST">
<label for="Email">Enter your name</label>
<input type="Email" id="email" name="email" required>
<button type="submit">send otp</button>
</form>
</body>
</html> """
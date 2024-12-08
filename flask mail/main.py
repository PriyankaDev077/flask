from flask import Flask,request,render_template_string,jsonify,session
from flask_mail import Mail, Message
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
<label for="Email">Enter your email</label>
<input type="Email" id="email" name="email" required>
<button type="submit">send otp</button>
</form>
</body>
</html> """
otp_verificaton_template="""
<!DOCTYPE html>
<html>
<head>
<title> verify otp </title>
</head>
<body>
<h1>enter the otp</h1>
<form action="/verify_otp" method="POST">
<label for="otp">enter otp</label>
<input type="text" id="otp" requried>
<button type="submit">verify otp</button>
</form></body>
</html>"""
@app.route('/')
def home():
    return render_template_string(otp_form_template)
@app.route('/send_otp',methods=["POST"])
def send_otp():
    email=request.form.get("email")
    if not email:
        return "email is required",400
    otp=str(random.randint(100000,999999))
    session['otp']=otp
    session['email']=email
    try:
        msg=Message(
        subject='your otp code',
        sender=app.config['mail_username'],
        recipients=[email],
        body=f'your otp is {otp}.it is valid for 10')
        mail.send(msg)
        return render_template_string(otp_verificaton_template)
    except Exception as e:
        return f'failed to send email: {str(e)}',500
@app.route('/verify_otp',methods=['POST'])
def verify_otp():
    entered_otp=request.form.get('otp')
    if not entered_otp:
        return "otp is required",400
    if "otp" in session and entered_otp==session['otp']:
        session.pop('otp',None)
        session.pop('email',None)
        return "<h1>otp verified succesfuly!!</h1>"
    else:
        return "<h1>invalied otp and please try again</h1>",400
@app.route('/favicon.ico')
def favicon():
    return "",204
if __name__=="__main__":
    app.run(debug=True)
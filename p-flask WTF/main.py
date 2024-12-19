from flask import Flask,request,render_template_string
app=Flask(__name__)
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        return f"thank you,{name}!your message has been received"
    template="""
<!DOCTYPE html>
<html>
<head>
<title>contact us</title>
</head>
<body>
<h1>contact us </h1>
<form method="POST">
<p>
<label for="name">name:</label>
<br>
<input type="text" name="name" id="name" required>
</p>
<p>
<label for="email">email:</label>
<br>
<input type="text" email="email" id="email" required>
</p>
<p>
<label for="message">message:</label>
<br>
<textarea name="message" id="message" rows='5'required></textarea>
</p>
<p>
<button type="submit">submit</button></p>
</form>
</body>
</html>"""
    return render_template_string(template)
if __name__== '__main__':
    app.run(debug=True)
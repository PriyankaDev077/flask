from flask import Flask, request, redirect,url_for
app=Flask(__name__)
app.secret_key='your_secret_key'
USERNAME='duckey'
PASSWORD='sugga07'
@app.route('/',methods=['GET'])
def login_form():
    return ''' 
    <!DOCTYPE HTML>
    <html lang='en'>
    <head>
    <title>
    login
    </title>
    </head>
    <body>
    <h2>
    login
    </h2>
    <form action="/login" method="post">
    <label for ="username">username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for ="password">password:</label>
    <input type="text" id="password" name="password"><br><br>
    <input type="submit" value="login">
        </form>
            </body>
                </html> '''
@app.route("/login",methods=["POST"])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    if username==USERNAME and password==PASSWORD:
        return '''
        <!DOCTYPE html>
        <html lang='en'>
        <head>
        <meta charset="UTF-8">
        <title>Welcome</title>
        </head>
        <body>
        <h2>Welcome,{}</h2>
        <p>you are successfully loggedin!</p>
        </body>
        </html>'''.format(username)
    else:
        return"""
        <!DOCTYPE html>
        <html lang='en'>
        <head><meta charset="UTF-8">
        <title>Welcome</title>
        </head>
        <body>
        <h2>login failed</h2>
        <p>incorrect username or password please try again</p>
        <a href='/'>back to login</a>
        </body>
        </html>"""
if __name__=='__main__':
    app.run(debug=True)        
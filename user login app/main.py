from flask import Flask, request, redirect,url_for
app=Flask(__name__)
app.secret_key='your_secret_key'
USERNAME='priyanka07'
PASSWORD='priy1nk1'
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
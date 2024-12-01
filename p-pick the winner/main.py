from flask import Flask,request,redirect,url_for
app=Flask(__name__)
votes ={'Cricket':0,'Football':0}
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
<input type='radio' name='choice' value='Cricket' required>Cricket
</label><br>
<label>
<input type='radio' name='choice' value='Football' required>Football
</label><br><br>
<button type='submit'>vote</button>
</form>
<h2>current votes</h2>
<ul>
<li>Cricket: {votes['Cricket']}</li>
<li>Football: {votes['Football']}</li></ul>
<form method='POST' action='/reset'>
<button type='submit'>reset votes</button></form>
</body>
</html>
"""
@app.route('/vote',methods=['POST'])
def vote():
    choice=request.form.get('choice')
    if choice in votes:
        votes[choice]+=1
    return redirect(url_for('index'))
@app.route('/reset',methods=['POST'])
def reset():
    global votes
    votes={key:0 for key in votes}
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)                
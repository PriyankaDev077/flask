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
<h2>current votes</h2>
<ul>
<li>team A: {votes['team A']}</li>
<li>team B: {votes['team B']}</li></ul>
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

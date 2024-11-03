from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():

 age = None

 if request.method == 'POST':

  birth_date = request.form.get('birth_date')

  if birth_date:

   try:

# Parse the input date

    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

# Calculate the age

    today = datetime.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

   except ValueError:

     age = "Invalid date format. Please enter a valid date."

# Replace render_template with a direct HTML response

 return f"""

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Age Calculator</title>

</head>

<body>

<h1>Calculate Your Age</h1>

<form method="POST">

<label for="birth_date">Enter your birth date:</label>

<input type="date" id="birth_date" name="birth_date" required>

<button type="submit">Calculate Age</button>

</form>

<h2>Your Age: {age if age is not None else "Enter your birth date."}</h2>

</body>

</html>

"""

if __name__ == '__main__':

 app.run(debug=True)
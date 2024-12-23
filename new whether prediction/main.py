from flask import Flask, request, render_template_string

import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual API key from OpenWeatherMap

API_KEY = 'ba5fe65e6989c100e0f5e80028c2f9c8'

HTML_TEMPLATE = '''

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Weather App</title>

</head>

<body>

<h1>Weather Prediction App</h1>

<form method="post">

<input type="text" name="city" placeholder="Enter city name" required>

<button type="submit">Get Weather</button>

</form>

{% if weather %}

<h2>Weather in {{ weather.city }}</h2>

<p>Temperature: {{ weather.temperature }} °C</p>

<p>Description: {{ weather.description }}</p>

<img src="http://openweathermap.org/img/wn/{{ weather.icon }}@2x.png" alt="Weather Icon">

{% endif %}

</body>

</html>

'''

def get_weather(city):

 url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

 response = requests.get(url)

 if response.status_code == 200:

  data = response.json()

  return {

'city': data['name'],

'temperature': data['main']['temp'],

'description': data['weather'][0]['description'],

'icon': data['weather'][0]['icon']

}

 else:

  return None

@app.route('/', methods=['GET', 'POST'])

def index():

 weather_data = None

 if request.method == 'POST':

  city = request.form.get('city')

  if city:

   weather_data = get_weather(city)
   
 return render_template_string(HTML_TEMPLATE, weather=weather_data)

if __name__ == '__main__':

 app.run(debug=True)
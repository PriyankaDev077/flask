from flask import Flask,request,render_template_string
import requests
app=Flask(__name__)
API_KEY="ba5fe65e6989c100e0f5e80028c2f9c8"
HTML_TEMPLATE="""
<!DOCTYPE html>
<html>
<head>
<title>
weather app
</title>
</head>
<body>
<h1>weather prediction app</h1>
<form method="post">
<input type='text' name='City' placeholder='Enter City Name' required>
<button type='submit'>get weather</button>
</form>
{% if weather %}
<h2>Weather in {{ weather.city }}</h2>
<p>Temperature: {{ weather.temperature }} °C</p>
<p>Description: {{ weather.description }}</p>
<img src="http://openweathermap.org/img/wn/{{ weather.icon }}@2x.png" alt="Weather Icon">
{% endif %}
</body>
</html>
"""
def get_weather(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return{
'city': data['name'],
'temperature': data['main']['temp'],
'description': data['weather'][0]['description'],
'icon': data['weather'][0]['icon']
        }
    else:
        return None
@app.route('/',methods=['GET','POST'])
def index():
    weather_data=None
    if request.method=='POST':
        city=request.form.get('city')
        if city :
            weather_data=get_weather(city)
    return render_template_string(HTML_TEMPLATE,weather=weather_data)
if __name__=="__main__":
    app.run(debug=True)            
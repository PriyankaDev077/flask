from flask import Flask
import folium
app=Flask(__name__)
@app.route('/')
def map_view():
    start_coords=(41.3874,2.1686)
    map_obj=folium.Map(location=start_coords,zoom_start=12)
    folium.Marker(location=start_coords,popup='Spain',tooltip='click for more info').add_to(map_obj)
    map_html=map_obj._repr_html_()
    html=f'''
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Location Map</title>
    </head>
    <body>
    <h1> locaton map app </h1>
    <div>
    {map_html}</div>
    </body>
    </html>
    '''
    return html
if __name__=='__main__':
    app.run(debug=True)
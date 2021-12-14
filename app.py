from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import config
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == "POST":
        raw_data = request.form["raw_data"]
        raw_data_array = raw_data.split('\n')
        location_data = []
        for i in raw_data_array:
            latlon = i.split(", ")
            url = "https://"+ config.url +"/v3/"+ config.api +"/reverse_geocoding?lat="+ latlon[0] +"&lon="+ latlon[1]
            responce = requests.get(url)
            location_info = responce.json()
            location_data.append(location_info)
        location_data_string = str(location_data)
        return location_data_string
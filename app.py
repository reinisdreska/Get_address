from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from geopy import Nominatim

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

geolocator = Nominatim(user_agent='MyGeoLocator')

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == "POST":
        raw_data = request.form["raw_data"]
        raw_data_array = raw_data.split('\n')
        location_data = []
        for i in raw_data_array:
            latlon = i.split(", ")
            geo_data = geolocator.reverse(i)
            address_info = geo_data.address.split(",")
            location_info = {
                "valsts":address_info[6],
                "admin_vien":address_info[4],
                "terit_vien":address_info[2],
                "apdz_vieta":address_info[3],
                "iela":address_info[1],
                "māja":address_info[0],
                "index":address_info[5],
                "adrese":address_info[1] + " " + address_info[0] + ", " + address_info[2] + ", " + address_info[3] + ", " + address_info[4] + ", " + address_info[6],
                "lat": latlon[0],
                "lon": latlon[1]
            }
            location_data.append(location_info)
        print(location_data)
        location_data_string = str(location_data)
        return location_data_string
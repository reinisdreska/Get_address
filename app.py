from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == "POST":
        raw_data = request.form["raw_data"]
        return raw_data
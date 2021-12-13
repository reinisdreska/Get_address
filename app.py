from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        raw_data = request.form["raw_data"]
        return raw_data
    return render_template("index.html")
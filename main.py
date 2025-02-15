from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route("/")
def home():
    with open("./data/data.json", "r") as file:
        # Parse the JSON data
        data = json.load(file)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
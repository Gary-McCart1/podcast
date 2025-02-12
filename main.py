from flask import Flask, render_template
import json


app = Flask(__name__)


# Open the local JSON file
with open("./data/data.json", "r") as file:
    # Parse the JSON data
    data = json.load(file)

# Now you can work with the `data` like any Python object

@app.route("/")
def home():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
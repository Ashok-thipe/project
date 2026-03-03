from flask import Flask, jsonify
import json

app = Flask(__name__)

DATA_FILE = "data.json"

@app.route("/api", methods=["GET"])
def get_data():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

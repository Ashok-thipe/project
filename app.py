from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

# Frontend Route (from master_1)
@app.route("/todo")
def todo():
    return render_template("todo.html")

# Backend Route (from master_2)
@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return "To-Do Item Saved Successfully!"

if __name__ == "__main__":
    app.run(debug=True)

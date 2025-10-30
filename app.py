from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Foydalanuvchi ma'lumotlarini o‘qish
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Ma’lumotlarni saqlash
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/click", methods=["POST"])
def click():
    user_id = request.json.get("user_id")
    data = load_data()
    if user_id not in data:
        data[user_id] = {"coins": 0}
    data[user_id]["coins"] += 1
    save_data(data)
    return jsonify({"coins": data[user_id]["coins"]})

@app.route("/balance/<user_id>")
def balance(user_id):
    data = load_data()
    coins = data.get(user_id, {}).get("coins", 0)
    return jsonify({"coins": coins})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

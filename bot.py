from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Faylga balans saqlanadi
BALANCE_FILE = "balances.json"

def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_balances(balances):
    with open(BALANCE_FILE, "w") as f:
        json.dump(balances, f)

@app.route("/get_balance", methods=["GET"])
def get_balance():
    user_id = request.args.get("user_id")
    balances = load_balances()
    balance = balances.get(user_id, 0)
    return jsonify({"balance": balance})

@app.route("/add_coin", methods=["POST"])
def add_coin():
    data = request.get_json()
    user_id = str(data["user_id"])
    balances = load_balances()
    balances[user_id] = balances.get(user_id, 0) + 1
    save_balances(balances)
    return jsonify({"balance": balances[user_id]})

@app.route("/")
def home():
    return "Azizbek Curipto bot ishlayapti ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

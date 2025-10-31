from flask import Flask, render_template, jsonify

app = Flask(__name__)

balance = 0  # vaqtinchalik balans

@app.route('/')
def home():
    return render_template('index.html', balance=balance)

@app.route('/add_coin', methods=['POST'])
def add_coin():
    global balance
    balance += 1
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

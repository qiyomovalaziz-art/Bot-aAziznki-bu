from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Foydalanuvchi balansi
user_balance = {
    "coins": 9
}

# Bosh sahifa
@app.route('/')
def index():
    return render_template('index.html', coins=user_balance["coins"])

# Vazifalar sahifasi
@app.route('/tasks')
def tasks():
    daily_tasks = [
        "Telegram kanalga obuna bo‘lish",
        "Postni do‘stlarga ulashish",
        "Botni do‘stga yuborish",
        "Har kuni botni ochish orqali bonus olish"
    ]
    return render_template('tasks.html', tasks=daily_tasks)

# Hamyon sahifasi
@app.route('/wallet')
def wallet():
    return render_template('wallet.html', coins=user_balance["coins"])

# Pul yechish (oddiy simulyatsiya)
@app.route('/withdraw')
def withdraw():
    if user_balance["coins"] >= 5:
        user_balance["coins"] -= 5
    return redirect(url_for('wallet'))

if __name__ == "__main__":
    app.run(debug=True)

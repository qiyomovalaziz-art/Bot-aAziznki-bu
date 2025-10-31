from flask import Flask, request, jsonify
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
import os
import asyncio
import threading

# ====== Flask ilovasi ======
app = Flask(__name__)

# ====== Telegram bot token ======
BOT_TOKEN = "7589550087:AAERu7icdx5z9Ye_hfM7-FwNwgtJVja0R_M"

# ====== Balans fayli ======
BALANCE_FILE = "balances.json"


# 🔹 Balansni yuklash
def load_balances():
    if os.path.exists(BALANCE_FILE):
        try:
            with open(BALANCE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


# 🔹 Balansni saqlash
def save_balances(balances):
    with open(BALANCE_FILE, "w") as f:
        json.dump(balances, f, indent=4)


# 🔹 /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💰 Tanga ishlash", url="https://web-production-cbda.up.railway.app/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Salom, {user.first_name}! 👋\n\n"
        "💎 Bu *Azizbek Curipto* mini ilovasi.\n"
        "👇 Quyidagi tugmani bosing va tanga ishlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


# 🔹 /balans komandasi
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    balances = load_balances()
    user_balance = balances.get(user_id, 0)

    await update.message.reply_text(
        f"💰 Sizning balansingiz: *{user_balance} tanga*",
        parse_mode="Markdown"
    )


# 🔹 Flask API: balans olish
@app.route("/get_balance", methods=["GET"])
def get_balance():
    user_id = request.args.get("user_id")
    balances = load_balances()
    balance = balances.get(user_id, 0)
    return jsonify({"balance": balance})


# 🔹 Flask API: tanga qo‘shish
@app.route("/add_coin", methods=["POST"])
def add_coin():
    data = request.get_json()
    user_id = str(data.get("user_id"))

    balances = load_balances()
    balances[user_id] = balances.get(user_id, 0) + 1
    save_balances(balances)

    return jsonify({"balance": balances[user_id]})


# 🔹 Flask test sahifasi
@app.route("/")
def home():
    return "<h2>✅ Azizbek Curipto API ishlayapti!</h2>"


# 🔹 Telegram botni ishga tushurish
async def run_bot():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()

    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("balans", balance))

    print("🤖 Telegram bot ishga tushdi...")
    await app_bot.run_polling()


# 🔹 Flask serverni ishga tushurish
def run_flask():
    print("🌐 Flask server ishga tushdi...")
    app.run(host="0.0.0.0", port=8000)


# 🔹 Har ikkalasini parallel ishga tushurish
if __name__ == "__main__":
    threading.Thread(target=lambda: asyncio.run(run_bot())).start()
    run_flask()

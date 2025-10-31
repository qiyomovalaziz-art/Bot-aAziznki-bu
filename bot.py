from flask import Flask, request, jsonify
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
import os
import asyncio

app = Flask(__name__)

# ======  BOT TOKEN  ======
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")  # Railway'da Environmentdan olinadi

# ======  BALANS FAYLI  ======
BALANCE_FILE = "balances.json"


# ======  Balansni yuklash va saqlash  ======
def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_balances(balances):
    with open(BALANCE_FILE, "w") as f:
        json.dump(balances, f, indent=4)


# ======  Telegram /start komandasi  ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💰 Bosing va pul ishlang", url="https://sening-mini-app-urling.vercel.app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Salom, {user.first_name}! 👋\n"
        f"Bu *Azizbek Curipto* mini ilovasi.\n\n"
        f"💎 Bosib tangalar ishlang!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


# ======  Flask API-lar  ======

@app.route("/get_balance", methods=["GET"])
def get_balance():
    user_id = request.args.get("user_id")
    balances = load_balances()
    balance = balances.get(user_id, 0)
    return jsonify({"balance": balance})


@app.route("/add_coin", methods=["POST"])
def add_coin():
    data = request.get_json()
    user_id = str(data.get("user_id"))

    balances = load_balances()
    balances[user_id] = balances.get(user_id, 0) + 1
    save_balances(balances)

    return jsonify({"balance": balances[user_id]})


@app.route("/")
def home():
    return "<h2>✅ Azizbek Curipto API ishlayapti!</h2>"


# ======  Parallel ishlatish  ======
async def run_bot():
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    print("🤖 Bot ishga tushdi...")
    await app_bot.run_polling()


def run_flask():
    print("🌐 Flask server ishga tushdi...")
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Flask va Botni parallel ishlatamiz
    loop.create_task(run_bot())
    run_flask()

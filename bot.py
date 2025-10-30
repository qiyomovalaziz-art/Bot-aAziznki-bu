import telebot
import requests
import os

TOKEN = "BOT_TOKENINGNI_BU_YERGA_QO'Y"  # ← bu joyga token
WEBAPP_URL = "https://web-production-f93c8.up.railway.app"  # ← bu sening linking

bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 123456789  # o‘zingning Telegram ID’ingni bu yerga yoz

@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.chat.id)
    text = (
        "👋 Salom, bu yerda tanga to‘plash mumkin!\n\n"
        "👇 Quyidagi tugma orqali o‘zingizning sahifangizni oching:"
    )
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(
        "💰 Tanga to‘plash", url=f"{WEBAPP_URL}?user_id={user_id}"
    )
    markup.add(btn)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(commands=["balance"])
def balance(message):
    user_id = str(message.chat.id)
    res = requests.get(f"{WEBAPP_URL}/balance/{user_id}")
    data = res.json()
    bot.send_message(message.chat.id, f"💰 Sizda {data['coins']} ta tanga bor!")

@bot.message_handler(commands=["withdraw"])
def withdraw(message):
    bot.send_message(message.chat.id, "💼 Hamyon manzilingizni yuboring:")

    bot.register_next_step_handler(message, process_wallet)

def process_wallet(message):
    wallet = message.text
    bot.send_message(message.chat.id, "⏳ So‘rov yuborildi, admin tekshiryapti.")
    bot.send_message(
        ADMIN_ID,
        f"💸 {message.from_user.first_name} ({message.chat.id}) pul yechmoqchi.\n"
        f"Hamyon: {wallet}\nTasdiqlash uchun /confirm_{message.chat.id}",
    )

@bot.message_handler(func=lambda m: m.text.startswith("/confirm_"))
def confirm_withdraw(message):
    user_id = message.text.split("_")[1]
    bot.send_message(int(user_id), "✅ Pul yechish so‘rovi tasdiqlandi! Hamyoningizga tushdi.")
    bot.send_message(ADMIN_ID, "✅ Tasdiq muvaffaqiyatli amalga oshdi.")

print("Bot ishga tushdi...")
bot.infinity_polling()

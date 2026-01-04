import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('8059161110:AAFDAylNrZ1RAv9SH2Eqdjiquwg4fUl4mKo')
bot = telebot.TeleBot(8059161110:AAFDAylNrZ1RAv9SH2Eqdjiquwg4fUl4mKo)

ORDERS = {}
NOTES = {

    "physics": {
        "name": "UNIT MEASUREMENT",
        "price": 14,
        "drive_link": "https://drive.google.com/file/d/1g-sVF5wl_BFg2Vb2sn4AQ2Dy_3U3u4xo/view?usp=sharing",
        "emoji": "📘"
    }
}

YOUR_FAMPAY_UPI = "8439890504@fam"

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📚 Browse Materials", callback_data="buy"))
    markup.add(types.InlineKeyboardButton("❓ Help", callback_data="help"))
    
    bot.send_message(user_id, "🎓 Welcome to @STUDY_NEST_NOTES_HUB_BOT!\n\nPremium study materials for exam preparation\n\n⚡ Quick UPI payment + Instant PDF delivery!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "buy")
def show_materials(call):
    user_id = call.message.chat.id
    msg = "📚 Available Materials:\n\n"
    for key, note in NOTES.items():
        msg += f"{note['emoji']} {note['name']}\n💰 ₹{note['price']}\n\n"
    bot.send_message(user_id, msg)

@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_section(call):
    msg = f"""
❓ HOW TO BUY:

1️⃣ Click "Browse Materials"
2️⃣ Choose your material
3️⃣ Send payment via FamPay UPI
4️⃣ Send receipt screenshot
5️⃣ Get PDF instantly!

📧 Contact: @studynestowner
    """
    bot.send_message(call.message.chat.id, msg)

@bot.message_handler(func=lambda msg: True)
def default_handler(message):
    bot.send_message(message.chat.id, "👋 Use /start to browse materials")

print("Study Notes Bot started...")
bot.infinity_polling()

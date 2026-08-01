import os
import threading
import time
import requests
from flask import Flask
import telebot

# Render အတွက် Port Bind စေရန် Flask Web Server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive and running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Render Server အိပ်မပျော်သွားစေရန် မိနစ်အနည်းငယ်တိုင်း Self-Ping လုပ်ပေးသည့် Function
def keep_alive():
    url = "https://telegram-bot-829d.onrender.com"
    while True:
        time.sleep(240) # 4 မိနစ်တိုင်း တစ်ခါ နှိုးပေးမည်
        try:
            requests.get(url)
            print("Keep-alive ping sent!")
        except Exception as e:
            print(f"Ping error: {e}")

# Telegram Bot Token
BOT_TOKEN = "8810223968:AAHB9zKAFnKFrmPdvDI162KnCE-gI3b-WcI"
bot = telebot.TeleBot(BOT_TOKEN)

# Key နှင့် Code များ (Underscore များ ဖြုတ်ပြီး အမှန်ပြင်ထားပါသည်)
KEY_DATABASE = {
    "KEY0701": [
        "STARLINK-CODE-437465",
        "STARLINK-CODE-207441",
        "STARLINK-CODE-502453"
    ],
    "KEY101": [
        "STARLINK-CODE-400325",
        "STARLINK-CODE-181505",
        "STARLINK-CODE-238064"
    ],
    "KEY969": [
        "STARLINK-CODE-458072",
        "STARLINK-CODE-225711",
        "STARLINK-CODE-485377"
    ],
    "KEY092": [
        "STARLINK-CODE-882054",
        "STARLINK-CODE-446223",
        "STARLINK-CODE-754407"
    ],
    "KEY124": [
        "STARLINK-CODE-451261",
        "STARLINK-CODE-565168",
        "STARLINK-CODE-627148"
    ],
    "KEY647": [
        "STARLINK-CODE-232465",
        "STARLINK-CODE-101751",
        "STARLINK-CODE-878010"
    ],
    "KEY600": [
        "STARLINK-CODE-678383",
        "STARLINK-CODE-415681",
        "STARLINK-CODE-524210"
    ],
    "KEY001": [
        "STARLINK-CODE-302727",
        "STARLINK-CODE-510286",
        "STARLINK-CODE-428854"
    ],
    "KEY650": [
        "STARLINK-CODE-562710",
        "STARLINK-CODE-144444",
        "STARLINK-CODE-585106"
    ]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ Starlink Code များ ရယူရန် သင်၏ Key ကို ရိုက်ထည့်ပေးပါ။")

@bot.message_handler(func=lambda message: True)
def process_key(message):
    # အက္ခရာ အကြီး/အသေး နှင့် စာလုံးကြား အလွတ်များကို ညှိပေးခြင်း
    user_key = message.text.strip().upper().replace("_", "")
    
    if user_key in KEY_DATABASE:
        codes = KEY_DATABASE[user_key]
        response_text = "Key မှန်ကန်ပါသည်။\n\nသင်၏ Starlink Code (၃) ခုမှာ -\n\n"
        for idx, code in enumerate(codes, 1):
            response_text += f"{idx}. `{code}`\n"
        
        bot.reply_to(message, response_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "Key မမှန်ပါ သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ။")

if __name__ == "__main__":
    # Flask Web Server Run မည်
    threading.Thread(target=run_flask, daemon=True).start()
    # Server မအိပ်စေရန် Self Ping Run မည်
    threading.Thread(target=keep_alive, daemon=True).start()
    
    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

import os
import threading
import time
import requests
from flask import Flask
import telebot

# ----------------------------------------------------
# Render Port Binding အတွက် Flask Web Server
# ----------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active and running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Render Server မအိပ်သွားအောင် Auto Ping ပို့ပေးသည့် Function
def keep_alive():
    url = "https://telegram-bot-829d.onrender.com"
    while True:
        time.sleep(240) # ၄ မိနစ်တိုင်း ping မည်
        try:
            requests.get(url)
            print("Keep-alive ping successful.")
        except Exception as e:
            print(f"Ping error: {e}")

# ----------------------------------------------------
# Telegram Bot Token & Configuration
# ----------------------------------------------------
BOT_TOKEN = "8810223968:AAHB9zKAFnKFrmPdvDI162KnCE-gI3b-WcI"
bot = telebot.TeleBot(BOT_TOKEN)

# Key နှင့် သက်ဆိုင်ရာ Starlink Codes Database
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

# သုံးပြီးသား Key များကို မှတ်ထားမည့်နေရာ
used_keys = set()

# ----------------------------------------------------
# Message Handlers
# ----------------------------------------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ Starlink Code များ ရယူရန် သင်၏ Key ကို ရိုက်ထည့်ပေးပါ။")

@bot.message_handler(func=lambda message: True)
def process_key(message):
    # စာလုံးအကြီးအသေး သန့်စင်ခြင်း နှင့် '_' ဖြုတ်ပေးခြင်း
    user_key = message.text.strip().upper().replace("_", "")
    
    # ၁။ Key ရှိမရှိ စစ်ဆေးခြင်း
    if user_key in KEY_DATABASE:
        # ၂။ Key သုံးပြီးပြီလား စစ်ဆေးခြင်း
        if user_key in used_keys:
            bot.reply_to(message, f"⚠️ {user_key} ကို ထုတ်ယူပြီး ဖြစ်ပါသည်။ ထပ်မံ အသုံးပြု၍ မရတော့ပါ။")
        else:
            # ၃။ မသုံးရသေးလျှင် Code ပို့ပေးပြီး သုံးပြီးသားအဖြစ် မှတ်လိုက်ခြင်း
            used_keys.add(user_key)
            codes = KEY_DATABASE[user_key]
            
            response_text = "Key မှန်ကန်ပါသည်။\n\nသင်၏ Starlink Code (၃) ခုမှာ -\n\n"
            for idx, code in enumerate(codes, 1):
                response_text += f"{idx}. `{code}`\n"
                
            bot.reply_to(message, response_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Key မမှန်ပါ သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ။")

# ----------------------------------------------------
# Main Execution Block
# ----------------------------------------------------
if __name__ == "__main__":
    # Flask Web Server Run မည်
    threading.Thread(target=run_flask, daemon=True).start()
    # Server မအိပ်စေရန် Self Ping Run မည်
    threading.Thread(target=keep_alive, daemon=True).start()
    
    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

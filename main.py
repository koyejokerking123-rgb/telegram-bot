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
# Telegram Bot Token Configuration
# ----------------------------------------------------
BOT_TOKEN = "8810223968:AAHB9zKAFnKFrmPdvDI162KnCE-gI3b-WcI"
bot = telebot.TeleBot(BOT_TOKEN)

# ----------------------------------------------------
# စခရင်ရှော့ (၁၀) ပုံမှ ဖတ်ယူထားသော Key နှင့် Code များ Database
# ----------------------------------------------------
KEY_DATABASE = {
    "KEY839": [
        "STARLINK-CODE-242546", # 3h
        "STARLINK-CODE-383132", # 1h30m
        "STARLINK-CODE-365486"  # 1h30m
    ],
    "KEY417": [
        "STARLINK-CODE-777841", # 3h
        "STARLINK-CODE-324851", # 1h30m
        "STARLINK-CODE-420501"  # 1h30m
    ],
    "KEY952": [
        "STARLINK-CODE-317502", # 3h
        "STARLINK-CODE-586250", # 1h30m
        "STARLINK-CODE-208373"  # 1h30m
    ],
    "KEY284": [
        "STARLINK-CODE-502453", # 3h
        "STARLINK-CODE-304588", # 1h30m
        "STARLINK-CODE-406846"  # 1h30m
    ],
    "KEY613": [
        "STARLINK-CODE-521278", # 3h
        "STARLINK-CODE-510643", # 1h30m
        "STARLINK-CODE-716814"  # 1h30m
    ],
    "KEY175": [
        "STARLINK-CODE-754407", # 3h
        "STARLINK-CODE-614517", # 1h30m
        "STARLINK-CODE-656480"  # 1h30m
    ],
    "KEY538": [
        "STARLINK-CODE-627148", # 3h
        "STARLINK-CODE-212543", # 1h30m
        "STARLINK-CODE-626623"  # 1h30m
    ],
    "KEY391": [
        "STARLINK-CODE-415681", # 3h
        "STARLINK-CODE-077322", # 1h30m
        "STARLINK-CODE-437465"  # 1h30m
    ],
    "KEY746": [
        "STARLINK-CODE-510286", # 3h
        "STARLINK-CODE-746617", # 1h30m
        "STARLINK-CODE-207441"  # 1h30m
    ],
    "KEY820": [
        "STARLINK-CODE-562710", # 3h
        "STARLINK-CODE-003116", # 1h30m
        "STARLINK-CODE-400325"  # 1h30m
    ],
    "KEY469": [
        "STARLINK-CODE-240345", # 3h
        "STARLINK-CODE-181505", # 1h30m
        "STARLINK-CODE-050281"  # 1h30m
    ],
    "KEY103": [
        "STARLINK-CODE-032425", # 3h
        "STARLINK-CODE-238064", # 1h30m
        "STARLINK-CODE-102705"  # 1h30m
    ],
    "KEY654": [
        "STARLINK-CODE-458072", # 1h30m
        "STARLINK-CODE-225711", # 1h30m
        "STARLINK-CODE-485377"  # 1h30m
    ],
    "KEY278": [
        "STARLINK-CODE-882054", # 1h30m
        "STARLINK-CODE-451415", # 1h30m
        "STARLINK-CODE-446223"  # 1h30m
    ],
    "KEY932": [
        "STARLINK-CODE-126774", # 1h30m
        "STARLINK-CODE-451261", # 1h30m
        "STARLINK-CODE-003530"  # 1h30m
    ],
    "KEY581": [
        "STARLINK-CODE-566688", # 1h30m
        "STARLINK-CODE-473162", # 1h30m
        "STARLINK-CODE-565168"  # 1h30m
    ],
    "KEY347": [
        "STARLINK-CODE-252532", # 1h30m
        "STARLINK-CODE-232465", # 1h30m
        "STARLINK-CODE-101751"  # 1h30m
    ],
    "KEY860": [
        "STARLINK-CODE-878010", # 1h30m
        "STARLINK-CODE-678383", # 1h30m
        "STARLINK-CODE-524210"  # 1h30m
    ],
    "KEY129": [
        "STARLINK-CODE-585762", # 1h30m
        "STARLINK-CODE-302727", # 1h30m
        "STARLINK-CODE-771272"  # 1h30m
    ],
    "KEY715": [
        "STARLINK-CODE-428854", # 1h30m
        "STARLINK-CODE-873048", # 1h30m
        "STARLINK-CODE-144444"  # 1h30m
    ],
    "KEY906": [
        "STARLINK-CODE-585106", # 1h30m
        "STARLINK-CODE-851184", # 1h30m
        "STARLINK-CODE-778658"  # 1h30m
    ],
    "KEY382": [
        "STARLINK-CODE-775186", # 1h30m
        "STARLINK-CODE-816081", # 1h30m
        "STARLINK-CODE-281881"  # 1h30m
    ],
    "KEY641": [
        "STARLINK-CODE-415180", # 1h30m
        "STARLINK-CODE-523808", # 1h30m
        "STARLINK-CODE-864151"  # 1h30m
    ],
    "KEY508": [
        "STARLINK-CODE-755504"  # 1h30m
    ]
}

# သုံးပြီးသား Key များကို မှတ်ထားမည့်နေရာ (Memory)
used_keys = set()

# ----------------------------------------------------
# Telegram Message Handlers
# ----------------------------------------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ Starlink Code များ ရယူရန် သင်၏ Key ကို ရိုက်ထည့်ပေးပါ။ (ဥပမာ- KEY839)")

@bot.message_handler(func=lambda message: True)
def process_key(message):
    # စာလုံးအကြီးအသေး သန့်စင်ခြင်း
    user_key = message.text.strip().upper()

    # ၁။ Key ရှိမရှိ စစ်ဆေးခြင်း (KEY ပါဝင်သော အမည် အပြည့်အစုံဖြင့်သာ စစ်ဆေးမည်)
    if user_key in KEY_DATABASE:
        # ၂။ Key ကို သုံးပြီးပြီလား စစ်ဆေးခြင်း
        if user_key in used_keys:
            bot.reply_to(message, f"⚠️ {user_key} ကို ထုတ်ယူပြီး ဖြစ်ပါသည်။ ထပ်မံ အသုံးပြု၍ မရတော့ပါ။")
        else:
            # ၃။ မသုံးရသေးပါက Code များ ပို့ပေးပြီး သုံးပြီးသားအဖြစ် မှတ်လိုက်ခြင်း
            used_keys.add(user_key)
            codes = KEY_DATABASE[user_key]
            
            response_text = "Key မှန်ကန်ပါသည်။\n\nသင်၏ Starlink Code များမှာ -\n\n"
            for idx, code in enumerate(codes, 1):
                response_text += f"{idx}. `{code}`\n"
                
            bot.reply_to(message, response_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "Key မမှန်ပါ သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ။")

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

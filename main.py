import telebot

BOT_TOKEN = "8810223968:AAHB9zKAFnKFrmPdvDI162KnCE-gI3b-WcI"
bot = telebot.TeleBot(BOT_TOKEN)

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
    "KEY_092": [
        "STARLINK-CODE-882054",
        "STARLINK-CODE-446223",
        "STARLINK-CODE-754407"
    ],
    "KEY_124": [
        "STARLINK-CODE-451261",
        "STARLINK-CODE-565168",
        "STARLINK-CODE-627148"
    ],
    "KEY_647": [
        "STARLINK-CODE-232465",
        "STARLINK-CODE-101751",
        "STARLINK-CODE-878010"
    ],
    "KEY_600": [
        "STARLINK-CODE-678383",
        "STARLINK-CODE-415681",
        "STARLINK-CODE-524210"
    ],
    "KEY_001": [
        "STARLINK-CODE-302727",
        "STARLINK-CODE-510286",
        "STARLINK-CODE-428854"
    ],
    "KEY_650": [
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
    user_key = message.text.strip()
    
    if user_key in KEY_DATABASE:
        codes = KEY_DATABASE[user_key]
        response_text = "Key မှန်ကန်ပါသည်။\n\nသင်၏ Starlink Code (၃) ခုမှာ -\n\n"
        for idx, code in enumerate(codes, 1):
            response_text += f"{idx}. `{code}`\n"
        
        bot.reply_to(message, response_text, parse_mode="Markdown")
    else:
        bot.reply_to(message, "Key မမှန်ပါ သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ။")

print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
bot.infinity_polling()

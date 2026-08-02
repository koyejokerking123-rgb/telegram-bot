import os
import telebot

# Telegram Bot Token ကို Render Environment Variable ကနေ ယူပါမည်
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Key များ နှင့် သက်ဆိုင်ရာ Starlink Code များ
KEY_DATABASE = {
    "KEY101": [
        "STARLINK-CODE-400325",
        "STARLINK-CODE-181505",
        "STARLINK-CODE-238064"
    ],
    "KEY092": [
        "STARLINK-CODE-111222",
        "STARLINK-CODE-333444",
        "STARLINK-CODE-555666"
    ]
}

# သုံးပြီးသား Key များကို မှတ်ထားရန် Set (Memory)
used_keys = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ Starlink Code များ ရယူရန် သင်၏ Key ကို ရိုက်ထည့်ပေးပါ။")

@bot.message_handler(func=lambda message: True)
def handle_key(message):
    user_input = message.text.strip().upper()

    # ၁။ Key မှန်မမှန် စစ်ဆေးခြင်း
    if user_input in KEY_DATABASE:
        # ၂။ Key ကို သုံးပြီးပြီလား စစ်ဆေးခြင်း
        if user_input in used_keys:
            bot.reply_to(message, f" {user_input} က ထုတ်ယူပြီးသား Key ဖြစ်ပါသည်။ ထပ်မံ အသုံးပြု၍ မရတော့ပါ။")
        else:
            # ၃။ မသုံးရသေးပါက Code များ ထုတ်ပေးပြီး သုံးပြီးသားအဖြစ် မှတ်လိုက်ခြင်း
            used_keys.add(user_input)
            codes = KEY_DATABASE[user_input]
            
            response = f"Key မှန်ကန်ပါသည်။\n\nသင်၏ Starlink Code ({len(codes)}) ခုမှာ -\n\n"
            for i, code in enumerate(codes, 1):
                response += f"{i}. {code}\n"
                
            bot.reply_to(message, response)
    else:
        bot.reply_to(message, " Key မမှန်ပါ သို့မဟုတ် သက်တမ်းကုန်ဆုံးသွားပါပြီ။")

if __name__ == "__main__":
    bot.infinity_polling()

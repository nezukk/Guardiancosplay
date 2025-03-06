#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7884843564:AAFqSQ4rAdtSBNclCiAws8s-p0W8fE5nu3Y")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28654544"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ffc3eee774bcb50e5bdc08f4abcb3a29")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002180531838"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6928010007"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://adamopytbusiness1:uSswEjo4ZHMGDU8Z@cluster0.gqgmk.mongodb.net/?retryWrites=true&w=majority&appName=CosplayGuardiansBot")
DB_NAME = os.environ.get("DATABASE_NAME", "CosplayGuardiansBot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002250921717"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002222453736"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://ibb.co/xtWc49Dr")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/Cp4ZQCYt")

#text
HELP_TXT = "<b>ʜɪ ᴅᴜᴅᴇ!!\nᴛʜɪs ɪs ᴀ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡʜɪᴄʜ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ : [ @Guardian_Station ]\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n💥 sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n🧑‍💻 ᴏᴡɴᴇᴅ ʙʏ : [ @Guardian_Station ]</b>"
ABOUT_TXT = "<b><blockquote>○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/OfflineByee'>Guardian</a>\n○ 𝐇-𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Guardian_Station'>𝐆ᴜᴀʀᴅɪᴀɴ 𝐒ᴛᴀᴛɪᴏɴ</a>\n○ 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/Hentai_Guardians_Adult>𝐇ᴇɴᴛᴀɪ 𝐆ᴜᴀʀᴅɪᴀɴ</a>\n○ 𝐉ᴀᴠ : <a href='https://t.me/Jav_Adult_Guardians'>𝐉ᴀᴠ </a></blockquote></b>"
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\n\nᴅᴇᴠᴇʟᴏᴘᴇᴅ ғᴏʀ : [ @Guardian_Station ] </b>")
try:
    ADMINS=[1683225887]
    for x in (os.environ.get("ADMINS", "1683225887").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "modijiurl.com")
SHORT_API = os.environ.get("SHORTNER_API", "fddc3e96107a11be9fe7557cdc4b59ced2a7c0bb")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - [ @Guardian_Station ]"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7827448605)

LOG_FILE_NAME = "savesama.txt"

LOG_FILE_NAME = "savesama.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 

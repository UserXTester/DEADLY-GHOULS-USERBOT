from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, deadlyversion
from pathlib import Path
import asyncio
import telethon.utils
DEADLY_GHOULS_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/c5148795f46fb78bab9b9.jpg"

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting DeadlyGhouls")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("DeadlyGhouls Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""CONGRATULATIONS 🥳🥳🎊🎊 YOUR DEADLY GHOULS BOT IS DEPLOYED 🎊 ... NOW TYPE .ping OR .alive TO CHECK OUR AMAZING BOT 🥳🔥 IF U HAVE ANY PROBLEM THEN JOIN @DEADLY_USERBOT""")
async def deadly_is_on():
    try:
        if Config.PM_LOGGR_BOT_API_ID != 0:
            await bot.send_file(
                Config.PM_LOGGR_BOT_API_ID,
                DEADLY_GHOULS_PIC,
                caption=f"᯽ ᒪᗴᘜᗴᑎᗪᖇY ᗩᖴ ᗪᗴᗩᗪᒪY ᘜᕼOᑌᒪՏ ᯽\n\n**𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ➪ {deadlyversion}**\n\n𝚃𝚈𝙿𝙴 `.ping` or `.alive` 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺! \n\n𝙹𝙾𝙸𝙽 [𝙳𝙴𝙰𝙳𝙻𝚈 𝙶𝙷𝙾𝚄𝙻𝚂 𝙲𝙷𝙰𝚃](t.me/DeadlyGhouls_CHIT_CHAT) 𝚃𝙾 𝚀𝚄𝙴𝚁𝚈 & 𝙹𝙾𝙸𝙽 [𝙳𝙴𝙰𝙳𝙻𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚂](t.me/DEADLY_TECHY) 𝚃𝙾 𝙺𝙽𝙾𝚆 𝚁𝙴𝙶𝚁𝙰𝙳𝙸𝙽𝙶 𝚄𝙿𝙳𝙰𝚃𝙴 𝙰𝙽𝙳 𝙽𝙴𝚆𝚂 𝙰𝙱𝙾𝚄𝚃 𝙳𝙴𝙰𝙳𝙻𝚈 𝙶𝙷𝙾𝚄𝙻𝚂 𝙱𝙾𝚃",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(deadly_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:            
    bot.run_until_disconnected()

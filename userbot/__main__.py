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

print(f"""CONGRATULATIONS π₯³π₯³ππ YOUR DEADLY GHOULS BOT IS DEPLOYED π ... NOW TYPE .ping OR .alive TO CHECK OUR AMAZING BOT π₯³π₯ IF U HAVE ANY PROBLEM THEN JOIN @DEADLY_TECHY""")
async def deadly_is_on():
    try:
        if Config.PM_LOGGR_BOT_API_ID != 0:
            await bot.send_file(
                Config.PM_LOGGR_BOT_API_ID,
                DEADLY_GHOULS_PIC,
                caption=f"α―½ αͺα΄αα΄ααͺαY α©α΄ αͺα΄α©αͺαͺY ααΌOααͺΥ α―½\n\n**ππ΄πππΈπΎπ½ βͺ {deadlyversion}**\n\nπππΏπ΄ `.ping` or `.alive` ππΎ π²π·π΄π²πΊ! \n\nπΉπΎπΈπ½ [π³π΄π°π³π»π πΆπ·πΎππ»π π²π·π°π](t.me/DeadlyGhouls_CHIT_CHAT) ππΎ πππ΄ππ & πΉπΎπΈπ½ [π³π΄π°π³π»π ππΏπ³π°ππ΄π](t.me/DEADLY_TECHY) ππΎ πΊπ½πΎπ ππ΄πΆππ°π³πΈπ½πΆ ππΏπ³π°ππ΄ π°π½π³ π½π΄ππ π°π±πΎππ π³π΄π°π³π»π πΆπ·πΎππ»π π±πΎπ",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(deadly_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:            
    bot.run_until_disconnected()

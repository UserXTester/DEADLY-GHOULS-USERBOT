
# Thanks to @D3_krish
# Porting in DeadlyGhouls by @OFFICIAL_SAMEER

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, deadlyversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DᴇᴀᴅʟʏGʜᴏᴜʟs"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

deadly = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/c5148795f46fb78bab9b9.jpg"
pm_caption = "  __**🔥🔥∂єα∂ℓу gнσυℓѕ 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={deadly})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{deadlyversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Channel:` [ᴊᴏɪɴ](https://t.me/DEADLY_USERBOT)\n"
pm_caption += f"┣•➳➠ `Creator:` [Himanshu](https://t.me/OFFICIAL_SAMEER)\n"
pm_caption += f"┣•➳➠ `Supporter:` [HellBoy](https://t.me/kraken_the_badass)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥REPO🔥](https://github.com/Deadly-fighters/DEADLY-GHOULS-BOT) 🔹 [📜License📜](https://github.com/Deadly-fighters/DEADLY-GHOULS-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()

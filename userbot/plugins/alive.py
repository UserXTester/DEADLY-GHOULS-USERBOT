
# Thanks to @D3_krish
# Porting in DeadlyGhouls by @OFFICIAL_SAMEER

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, deadlyversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "βΡΞ±ββΡ gΠ½ΟΟβΡ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

deadly = bot.uid

DEADLY_GHOULS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/c5148795f46fb78bab9b9.jpg"
pm_caption = "  __**π₯π₯βΡΞ±ββΡ gΠ½ΟΟβΡ πππ ππ ππππππ₯π₯**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 ππππππππ\n  **γπ[{DEFAULTUSER}](tg://user?id={deadly})πγ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `Telethon:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `Version:` `{deadlyversion}`\n"
pm_caption += f"β£β’β³β  `Sudo:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `Channel:` [α΄α΄ΙͺΙ΄](https://t.me/DEADLY_TECHY)\n"
pm_caption += f"β£β’β³β  `Creator:` [Himanshu](https://t.me/OFFICIAL_SAMEER)\n"
pm_caption += f"β£β’β³β  `Supporter:` [HellBoy](https://t.me/kraken_the_badass)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [π₯REPOπ₯](https://github.com/Deadly-fighters/DEADLY-GHOULS-BOT) πΉ [πLicenseπ](https://github.com/Deadly-fighters/DEADLY-GHOULS-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, DEADLY_GHOULS_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()

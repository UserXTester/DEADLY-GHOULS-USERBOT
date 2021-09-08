# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @official_sameer_the_badass from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from userbot import bot
from DeadlyGhouls.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(official_sameer):
    deadly = official_sameer.pattern_match.group(1)
    if not deadly:
        if official_sameer.is_reply:
            (await official_sameer.get_reply_message()).message
        else:
            await edit_or_reply(official_sameer, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(deadly))}")

    await troll[0].click(
        official_sameer.chat_id,
        reply_to=official_sameer.reply_to_msg_id,
        silent=True if official_sameer.is_reply else False,
        hide_via=True,
    )
    await official_sameer.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
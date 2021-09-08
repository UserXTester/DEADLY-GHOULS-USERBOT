import re

from DeadlyGhouls import bot
from DeadlyGhouls.utils import admin_cmd, sudo_cmd, edit_or_reply
from DeadlyGhouls.cmdhelp import CmdHelp
from DeadlyGhouls.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(official_sameer):
    mafia = official_sameer.pattern_match.group(1)
    if not mafia:
        if official_sameer.is_reply:
            (await official_sameer.get_reply_message()).message
        else:
            await edit_or_reply(official_sameer, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(mafia))}")

    await troll[0].click(
        official_sameer.chat_id,
        reply_to=official_sameer.reply_to_msg_id,
        silent=True if official_sameer.is_reply else False,
        hide_via=True,
    )
    await official_sameer.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()

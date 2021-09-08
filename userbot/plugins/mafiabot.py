import time

from userbot import ALIVE_NAME, StartTime, deadlyversion
from DeadlyGhouls.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon import events, version

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "DeadlyGhouls User"
DEADLY_GHOULS_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG 

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="deadly$"))
@bot.on(sudo_cmd(pattern="deadly$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DEADLY_GHOULS_IMG:
        deadly_caption = f"🔥 ℓєgєη∂яу αƒ ∂єα∂ℓу кααℓ 🔥\n\n"
        deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"
        deadly_caption += f"**{Config.ALIVE_MSG}**\n\n"
        deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"                
        deadly_caption += f"𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"
        deadly_caption += f"➾ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽` ➣ `{tel_ver}` \n"
        deadly_caption += f"➾ `𝚂𝚄𝙳𝙾 𝙼𝙾𝙳𝙴:` ➣ `{is_sudo}`\n"
        deadly_caption += f"➾ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_CHANNEL)\n"
        deadly_caption += f"➾ 𝙼𝚈 𝙶𝚁𝙾𝚄𝙿: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_GROUP)\n\n"
        deadly_caption += f"[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙳𝙴𝙰𝙳𝙻𝚈 𝙺𝙰𝙰𝙻 ✨](https://github.com/DEADLY-FIGHTERS/DEADLY-KAAL-BOT)\n" 
                                      await alive.client.send_file(
            alive.chat_id, DEADLY_GHOULS_IMG, caption=deadly_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"__**𝔹𝕆𝕋 𝕊𝕋𝔸𝕋𝕌𝕊**__\n\n"
            f"**★ 𝕋𝕖𝕝𝕖𝕥𝕙𝕠𝕟 𝕧𝕖𝕣𝕤𝕚𝕠𝕟 :** `{version.__version__}`\n"
            f"**★ ∂єα∂ℓу gнσυℓѕ :** `{deadlyversion}`\n"
            f"**★ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
            f"**★ 𝕄𝕒𝕤𝕥𝕖𝕣 :** {mention}\n",
        )

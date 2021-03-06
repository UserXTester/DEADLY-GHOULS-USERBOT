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
        deadly_caption = f"š„ āŃgŃĪ·āŃŃ Ī±Ę āŃĪ±āāŃ gŠ½ĻĻāŃ š„\n\n"
        deadly_caption += f"āāāāāāāāāāāāāāāāāāāāāāāāāāāā\n\n"
        deadly_caption += f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        deadly_caption += f"āāāāāāāāāāāāāāāāāāāāāāāāāāāā\n\n"                
        deadly_caption += f"š£ š°š±š¾šš š¼š ššššš“š¼ š£\n\n"
        deadly_caption += f"ā¾ `šš“š»š“šš·š¾š½` ā£ `{tel_ver}` \n"
        deadly_caption += f"ā¾ `ššš³š¾ š¼š¾š³š“:` ā£ `{is_sudo}`\n"
        deadly_caption += f"ā¾ š¼š š²š·š°š½š½š“š»: ā£ [š¹š¾šøš½](t.me/Config.YOUR_CHANNEL)\n"
        deadly_caption += f"ā¾ š¼š š¶šš¾ššæ: ā£ [š¹š¾šøš½](t.me/Config.YOUR_GROUP)\n\n"
        deadly_caption += f"[āØ š³š“šæš»š¾š šš¾šš š³š“š°š³š»š š¶š·š¾šš»š āØ](https://github.com/DEADLY-FIGHTERS/DEADLY-GHOULS-BOT)\n" 
        await alive.client.send_file(
            alive.chat_id, DEADLY_GHOULS_IMG, caption=deadly_caption, reply_to=reply_to_id
        )                  
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"š„ āŃgŃĪ·āŃŃ Ī±Ę āŃĪ±āāŃ gŠ½ĻĻāŃ š„\n\n"
            f"āāāāāāāāāāāāāāāāāāāāāāāāāāāā\n\n"
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"āāāāāāāāāāāāāāāāāāāāāāāāāāāā\n\n"                
            f"š£ š°š±š¾šš š¼š ššššš“š¼ š£\n\n"
            f"ā¾ `šš“š»š“šš·š¾š½` ā£ `{tel_ver}` \n"
            f"ā¾ `ššš³š¾ š¼š¾š³š“:` ā£ `{is_sudo}`\n"
            f"ā¾ š¼š š²š·š°š½š½š“š»: ā£ [š¹š¾šøš½](t.me/Config.YOUR_CHANNEL)\n"
            f"ā¾ š¼š š¶šš¾ššæ: ā£ [š¹š¾šøš½](t.me/Config.YOUR_GROUP)\n\n"
            f"[āØ š³š“šæš»š¾š šš¾šš š³š“š°š³š»š š¶š·š¾šš»š āØ](https://github.com/DEADLY-FIGHTERS/DEADLY-GHOULS-BOT)\n" 
           
        )

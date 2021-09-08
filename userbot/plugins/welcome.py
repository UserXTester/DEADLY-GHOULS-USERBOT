from telethon import events
from telethon.utils import pack_bot_file_id

from userbot.plugins.sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
    update_previous_welcome,
)
from DeadlyGhouls.utils import *
from userbot.cmdhelp import CmdHelp


@bot.on(events.ChatAction())  # pylint:disable=E0602
async def _(event):
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        # logger.info(event.stringify())
        """user_added=False,
        user_joined=True,
        user_left=False,
        user_kicked=False,"""
        if event.user_joined:
            if cws.should_clean_welcome:
                try:
                    await bot.delete_messages(  # pylint:disable=E0602
                        event.chat_id, cws.previous_welcome
                    )
                except Exception as e:  # pylint:disable=C0103,W0703
                    logger.warn(str(e))  # pylint:disable=E0602
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await bot.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name, a_user.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = (
                f"@{me.username}" if me.username else f"[Me](tg://user?id={me.id})"
            )
            userid = a_user.id
            current_saved_welcome_message = cws.custom_welcome_message
            mention = "[{}](tg://user?id={})".format(a_user.first_name, a_user.id)

            current_message = await event.reply(
                current_saved_welcome_message.format(
                    mention=mention,
                    title=title,
                    count=count,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                ),
                file=cws.media_file_id,
            )
            update_previous_welcome(event.chat_id, current_message.id)


@bot.on(admin_cmd(pattern="savewelcome", outgoing=True))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="savewelcome", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    if msg and msg.media:
        bot_api_file_id = pack_bot_file_id(msg.media)
        add_welcome_setting(event.chat_id, msg.message, True, 0, bot_api_file_id)
        await edit_or_reply(event, "Welcome note saved. ")
    else:
        input_str = event.text.split(None, 1)
        add_welcome_setting(event.chat_id, input_str[1], True, 0, None)
        await edit_or_reply(event, "Welcome note saved. ")


@bot.on(admin_cmd(pattern="clearwelcome", outgoing=True)) # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="clearwelcome", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cws = get_current_welcome_settings(event.chat_id)
    rm_welcome_setting(event.chat_id)
    await edit_or_reply(event, 
        "Welcome note cleared. "
        + "The previous welcome message was `{}`.".format(cws.custom_welcome_message)
    )


@bot.on(admin_cmd(pattern="listwelcome", outgoing=True)) # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="listwelcome", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if hasattr(cws, "custom_welcome_message"):
        await edit_or_reply(event, 
            "Welcome note found. "
            + "Your welcome message is\n\n`{}`.".format(cws.custom_welcome_message)
        )
    else:
        await edit_or_reply(event, "No Welcome Message found")

CmdHelp("welcome").add_command(
  "listwelcome", None, "Gets the saved welcome message of DeadlyGhouls"
).add_command(
  "clearwelcome", None, "Clears/Deletes the welcome message (if any)"
).add_command(
  "savewelcome", "<reply to msg>", "Saves the replied msg as welcome note from you."
).add()
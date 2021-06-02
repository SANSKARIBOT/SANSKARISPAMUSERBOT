import time

from userbot import ALIVE_NAME, StartTime, sanskariversion
from sanskaribot.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "sanskari User"
sanskari_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGENDARY AF SANSKARIBOT"

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


@bot.on(admin_cmd(outgoing=True, pattern="sanskari$"))
@bot.on(sudo_cmd(pattern="sanskari$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if sanskari_IMG:
        sanskari_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        sanskari_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        sanskari_caption += f"__**BOT STATUS**__\n\n"
        sanskari_caption += f"**★ TELETHON VERSION :** `1.15.0`\n"
        sanskari_caption += f"**★ SANSKARIBOT :**`{sanskariversion}`\n"
        sanskari_caption += f"**★ UPTIME :** `{uptime}\n`"
        sanskari_caption += f"**★ MASTER :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, sanskari_IMG, caption=sanskari_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"__**BOT STATUS**__\n\n"
            f"**★ TELETHON VERSION :** `1.15.0`\n"
            f"**★ SANSKARIBOT :** `{sanskariversion}`\n"
            f"**★ UPTIME :** `{uptime}\n`"
            f"**★ MASTER :** {mention}\n",
        )


import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, sanskariversion
from sanskaribot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "sanskari"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

sanskari = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2e643737d77e815384136.mp4"
file2 = "https://telegra.ph/file/8ded72864a2a26931a8ab.jpg"
file3 = "https://telegra.ph/file/2e643737d77e815384136.mp4"
file4 = "https://telegra.ph/file/8ded72864a2a26931a8ab.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥 SANSKARIBOT IS ALIVE 🔥🔥**__\n\n"

pm_caption += (
    f"                 👑MASTER👑\n**  『😈[{DEFAULTUSER}](tg://user?id={sanskari})😈』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n\n"

pm_caption += f"😈SANSKARIBOT😈 : `{sanskariversion}`\n\n"

pm_caption += f"😱SUDO😱            : `{sudou}`\n\n"

pm_caption += "😇CHANNEL😇️   : [ᴊᴏɪɴ](https://t.me/CHICKENMOD)\n\n"

pm_caption += "😎CREATOR😎    : [Shubham](https://t.me/SHUBHAM_ROOTER)\n\n"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    

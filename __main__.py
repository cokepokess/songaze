# Leo Projects <https://t.me/leosupportx>
# @Naviya2 π±π°

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from LeoSongDownloaderBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LeoSongDownloaderBot import LeoSongDownloaderBot as app
from LeoSongDownloaderBot import LOGGER

pm_start_text = """
Hello [{}](tg://user?id={}) π

I'm Leo Song Downloader Bot π±π°

You can download any song within a shortime with this Bot π

If you want to know how to use this bot just
touch on this command " /help " π

Leo Projects π±π°
"""

help_text = """
You should know the following commands to use this bot π

β­οΈ /song <song name>: Download songs from all sources π

β­οΈ Send youtube url to me directly i can download it to your telegram database in audio format π


Made By : @naviya2 π±π°
Support Group : @leosuppportx π±π°
Updates Channel : @new_ehi π±π°
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         text="Updates Channelπ£", url="https://t.me/new_ehi"
                    ),
                    InlineKeyboardButton(
                        text="Support Groupπ₯", url="https://t.me/leosupportx"
                    ),
                ],
                    
                [
                    InlineKeyboardButton(
                        text="Developerπ§βπ»", url="https://t.me/naviya2"
                    ),
                    InlineKeyboardButton(
                        text="Rate us β", url="https://t.me/tlgrmcbot?start=leosongdownloaderbot-review"
                    ),     
                ],
                
                [
                    InlineKeyboardButton(
                        text="β Add me to your group β", url="t.me/leosongdownloaderbot?startgroup=true"
                    ),
                ],
            ],
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("LeoSongDownloaderBot is online.")
idle()

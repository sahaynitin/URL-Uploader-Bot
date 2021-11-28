#https://github.com/PredatorHackerzZ/RENAMER-BOT


import os
import sqlite3
import logging
import pyrogram

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from pyrogram import filters
from scripts import Scripted
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Clinton.on_message(filters.command(["start"]))
async def start(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.START_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='⭕ Update Channel⭕', url=f'https://t.me/{Config.UPDATE_CHANNEL}'),
                                                 InlineKeyboardButton(text='⭕ Support Group⭕', url=f'https://t.me/{Config.UPDATE_GROUP}') ],
                                              [ [ InlineKeyboardButton(text='🔐 ᴄʟᴏꜱᴇ 🔐', callback_data='close') ],
                                                  InlineKeyboardButton(text='⭕ Help ⭕', callback_data='help') ] ] ]

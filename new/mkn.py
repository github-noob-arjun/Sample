from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from Client.client import Clt2

@Clt2.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Success Message 💥 1")

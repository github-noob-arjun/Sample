from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
import asyncio

DltBot = Client(
      "app1",
      bot_token="5592815069:AAFdddkNDJ4xKxkIOlEzOOjnwX8ieW7huiY",
      api_id="4738674",
      api_hash="f2be74eaa9b1cb32498f45d04e4dbb54",
)

media_filter = filters.document | filters.video | filters.audio
CHANNELS = [-1001527733655, -1001527733655]

@DltBot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply("**✅ Bot working\n\n⚠️This is private Bot. You can't Access**")

@DltBot.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    await asyncio.sleep(18000) 
    await message.delete()

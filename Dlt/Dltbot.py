from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
import asyncio

DltBot = Client(
      "app1",
      bot_token="5589185991:AAGDjCCcp7IG1u_YQErui5yLwyfXizptXYI",
      api_id="4738674",
      api_hash="f2be74eaa9b1cb32498f45d04e4dbb54",
)

media_filter = filters.document | filters.video | filters.audio

@DltBot.on_message(filters.command("start")
async def start(bot, message):
    await message.reply("**✅ Bot working**")

@DltBot.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    await asyncio.sleep(10) 
    await message.delete()

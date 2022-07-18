from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 


MKN = Client(
      "protester",
      bot_token="5589185991:AAGDjCCcp7IG1u_YQErui5yLwyfXizptXYI",
      api_id="4738674",
      api_hash="f2be74eaa9b1cb32498f45d04e4dbb54",
)

@MKN.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Success Message 💥 1")

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 


MKN = Client(
      "protester",
      bot_token="5589185991:AAGDjCCcp7IG1u_YQErui5yLwyfXizptXYI",
      api_id="4738674",
      api_hash="f2be74eaa9b1cb32498f45d04e4dbb54",
)

CMD = [".", "/"]

@MKN.on_message(filters.command(["start"], CMD))
async def info(mkn, msg):
    await msg.reply_text(
        text="Hello Bro sugamaano 😉",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("💥💥", callback_data="about")
            ]]
            )
        )

@MKN.on_message(filters.command(["h"], CMD))
async def info(mkn, msg):
    await msg.reply_sticker(
        sticker="CAADBQADsQIAAtILIVYld1n74e3JuQI"
    )

@MKN.on_message(filters.command(["help"], CMD))
async def info(mkn, msg):
    await msg.reply_sticker(
        sticker="CAADBQADEgQAAtMJyFVJOe6-VqYVzAI"
    )


@MKN.on_callback_query()
async def callback_data(client, query: CallbackQuery):
    data = query.data 
    if data == "about":
        await query.answer("┣⪼🚀 𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙷𝙴𝚁𝚄𝙺𝙾\n┣⪼🍀 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 : 𝙼𝙾𝚃𝙾𝚁 𝙰𝚂𝚈𝙽𝙲𝙾\n┣⪼🗂️ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚁𝙾𝙶𝚁𝙰𝙼\n┣⪼📃 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 3\n┣⪼👨‍💻 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : 𝙹𝚎𝚘𝚕", show_alert=True)




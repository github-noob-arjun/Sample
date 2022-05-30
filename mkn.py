from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 


MKN = Client(
      "protester",
      bot_token="5231845980:AAEZoyG-mykf7-5d8zFx_X_RWcWBv_SUP0M",
      api_id="6152295",
      api_hash="2d291700c03d39c4fdb7092d1f34f07c",
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


print("💥BOT IS STARTLED🚀")        
MKN.run()


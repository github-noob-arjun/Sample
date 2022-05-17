from pyrogram import Client, filters


MKN = Client(
      "id bot",
      bot_token="5231845980:AAHLyejUGI9C6EanZK7id7QSI-iVIWEoJZ8",
      api_id="6152295",
      api_hash="2d291700c03d39c4fdb7092d1f34f07c",
)

CMD = [".", "/"]

@MKN.on_message(filters.command(["start"], CMD))
async def info(mkn, msg):
    await msg.reply_sticker(
        sticker="CAADBQADsQIAAtILIVYld1n74e3JuQI"
    )

@MKN.on_message(filters.command(["help"], CMD))
async def info(mkn, msg):
    await msg.reply_sticker(
        sticker="CAADBQADEgQAAtMJyFVJOe6-VqYVzAI"
    )


        
MKN.run()

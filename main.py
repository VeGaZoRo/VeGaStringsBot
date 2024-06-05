import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
VeGa = VeGa(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="VeGaSTRINGBOT"),
)


if __name__ == "__main__":
    print("𝖲𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝖸𝐨𝐮𝐫 𝖲𝐭𝐫𝐢𝐧𝐠 𝖡𝐨𝐭...")
    try:
        VeGa.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = VeGa.get_me().username
    print(f"@{uname} 𝖲𝖳𝖠𝖱𝖳𝖤𝖣 𝖲𝖴𝖢𝖤𝖲𝖲𝖥𝖴𝖫𝖫𝖸. 𝖬𝖠𝖣𝖤 𝖡𝖸 @ 𝖣𝖠𝖷𝖷 𝖳𝖤𝖠𝖬 🤗")
    idle()
    VeGa.stop()
    print("𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗!")

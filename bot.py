#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

from pyrogram import Client, __version__

from config import Config
from config import LOGGER

from user import User
from pyrogram import Client

class Bot(Client):
    USER = None
    USER_ID = None

    def __init__(self):
        name = "my_bot"
        session_name = "AQFplNMAt_g3Zo403aPpTa3f77dXHu6H0SOspgpCbdMNi18PvJRAnWRQEchkrx-_pItrk9wwIiSBpqI-NM7lBculnsPeLGcb6cd-L__9ZbmhGe4pBNwpLyRy4dTK_UNoAtoJb1YcCexcF-L59iv0SEYOlFlsRMp9FQ8iZS27K9OlVEOBUc-_3vMNMzr_vfSttITeL1Z1XJM4eQVflfgb1fDAhJ_dtsVvq7MRjIqdQtG_jPFvXQI9sPH7kudugQpe0tssa2CAUMuXAUfEP_FBEKkYTpb_3uJRJbt6YIGIa5S8v70j-Z6sD0zVOE1qJVYx36G7Z4dgN0tfYdJEBun5vBA3AD0P3AAAAAFI7DftAA"  # Add your desired session name here
        super().__init__(
            session_name,
            api_hash="a5b4f74cd5b550622c4eee4fea7285b0",
            api_id=23696595,  # Replace with your API ID
            plugins={"root": "plugins"},
            workers=4,
            bot_token="YOUR_BOT_TOKEN"
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started!"
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")


bot = Bot()
bot.run()

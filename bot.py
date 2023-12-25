#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

from telethon.sync import TelegramClient, events

class Bot(TelegramClient):
    USER = None
    USER_ID = None

    def __init__(self):
        api_id = 23696595  # Replace with your API ID
        api_hash = 'a5b4f74cd5b550622c4eee4fea7285b0'  # Replace with your API hash
        session_name = '1AZWarzoBu16jHqFBvPYZMWTX7q5E2ja075bMIUr21lxTR_FlpL85wyB4Lazrt0-Xw8ZVsGFddzlWTnVwhY7OeQfBCySjYW9NU7U6Mtw1Qlbx7rO9fH-lWOQiWEabafR6wW-Pekxrfsmct-dKcM-gvkQiDhtcU7h8YTJ2uDPWI2oOALuXLS6oZyvTmyJYZfh89GzFkp9exzMoWZFegM3eg48ea_YLfrCVvsbrdbK_tBq8InAM6DWZlhtzMfqwnspnmp13edEhSq2GqLM7oHSkIblTUY7sSxWAN_DPbtJ4rAlXDUDN6YmN9hdGg_OpHmUec3UQLHXJOh0jLK5jdErfHyU0RV6TO80='  # Add your desired session name here

        super().__init__(
            session_name,
            api_id,
            api_hash
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.LOGGER(name).info(
            f"@{usr_bot_me.username} started!"
        )
        self.USER, self.USER_ID = await self.get_me()

    async def stop(self, *args):
        await super().disconnect()
        self.LOGGER(name).info("Bot stopped. Bye.")


bot = Bot()

# Register event loop to handle stop
@bot.on(events.NewMessage(pattern='/stop'))
async def stop_bot(event):
    await bot.stop()

bot.start()
bot.run_until_disconnected()

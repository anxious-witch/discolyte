from discord.ext import commands
from dotenv import load_dotenv
from typing import NoReturn
import discord
import modules
import asyncio
import aiohttp
import os

class Acolyte(commands.AutoShardedBot):
    extensions = {
        "modules.chat",
        "modules.loader",
    }

    def __init__(self, token: str) -> None:
        self.token = token
        super().__init__(
            command_prefix=commands.when_mentioned_or("~"),
            description="Hi! I'm Acolyte!"
        )
        self.__load_extensions()

    def __load_extensions(self) -> None:
        print("Loading extensions...")
        for extension in self.extensions:
            try:
                self.load_extension(extension)
                print(f"Extension {extension} loaded.")
            except (AttributeError, ImportError) as ex:
                print(f"Failed to load module {extension}!")
                print(str(ex))


    async def on_ready(self) -> None:
        print("Acolyte ready!")

    def run(self) -> None:
        super().run(self.token)

if __name__ == "__main__":
    load_dotenv()
    acolyte = Acolyte(os.getenv("BOT_TOKEN"))

    acolyte.run()

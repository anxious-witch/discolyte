from discord.ext import commands
import discord
import asyncio
import aiohttp
import os

class Acolyte(commands.AutoShardedBot):
    extensions = {
        "acolyte.modules.chat",
        "acolyte.modules.loader",
        "acolyte.modules.audio",
    }

    def __init__(self, token: str) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or("~"),
            description="Hi! I'm Acolyte!"
        )

        self.token = token
        self.session = aiohttp.ClientSession(
            loop=self.loop,
            connector=aiohttp.TCPConnector(verify_ssl=True)
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


    """ Fired when the bot is resdy for events """
    async def on_ready(self) -> None:
        print("Acolyte ready!")

    """ Override the inherited class' close method to close the aiohttp session """
    async def close(self) -> None:
        print("Closing connections and cleaning up.")

        await super().close()
        await self.session.close()

    """ Run the bot """
    def run(self) -> None:
        super().run(self.token)

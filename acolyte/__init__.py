import aiohttp
from pathlib import Path
from discord.ext import commands
from watchdog.observers import Observer
from acolyte.util.watchdog import FileHandler


class Acolyte(commands.AutoShardedBot):
    extensions = {
        "acolyte.modules.chat",
        "acolyte.modules.loader",
        "acolyte.modules.nightcore",
    }

    def __init__(self, token: str, development=False) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or("~"),
            description="Hi! I'm Acolyte!"
        )

        self.token = token
        self.session = aiohttp.ClientSession(
            loop=self.loop,
            connector=aiohttp.TCPConnector(verify_ssl=True)
        )
        self.development = development

        if self.development:
            # Start the file observer
            print("[DEV] Starting watchdog")

            self.observer = Observer()
            path = str(Path("./acolyte/modules"))
            handler = FileHandler(self)

            self.observer.schedule(handler, path)
            self.observer.start()

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

    """ Fired after watchdog detects a file change """
    def reload_extension(self, extension_name) -> None:
        extension = f"acolyte.modules.{extension_name}"

        # There's something quirky going on with reload_extension
        # So I unload and then load it again instead...
        if extension in self.extensions:
            self.unload_extension(extension)
            self.load_extension(extension)
            print(f"Extension {extension} reloaded.")

    """ Fired when the bot is resdy for events """
    async def on_ready(self) -> None:
        print("Acolyte ready!\n")

    """ Override the inherited class' close method to clean up """
    async def close(self) -> None:
        print("Closing connections and cleaning up.")

        await super().close()
        await self.session.close()

        if self.development:
            self.observer.stop()

            # Join with the main thread for a party
            self.observer.join()

    """ Run the bot """
    def run(self) -> None:
        super().run(self.token)

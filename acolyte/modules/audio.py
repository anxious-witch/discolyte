import discord
import aiohttp
import ffmpeg
import subprocess
from io import BytesIO
from discord.ext import commands
from mimetypes import guess_extension

from acolyte.util.http import Http

class Audio(commands.Cog):
    """ Post-avant jazzcore"""

    file_extension_whitelist = {
        ".mp3",
        ".wav",
        ".ogg",
        ".aac",
        ".flac",
    }

    def __init__(self, bot):
        self.bot = bot
        self.http = Http(self.bot.session)

    async def __get_extension(self, url: str):
        headers = await self.http.get_headers(url)

        if headers is not None:
            extension_maybe = guess_extension(headers["Content-Type"])
            if extension_maybe == ".oga":
                extension_maybe == ".ogg"

            return extension_maybe

    @commands.command()
    async def nightcore(self, ctx):
        """ ONE TWO SEVEN THREE DOWN TO ROCKEFELLER STREET """
        if len(ctx.message.attachments) > 0:
            # Just get the first one for now
            attachment = ctx.message.attachments[0]
            filename = attachment.filename
            url = attachment.url

            extension = await self.__get_extension(url)

            if extension not in self.file_extension_whitelist:
                return await ctx.send("That's probably not a sound file! Maybe!!")

            song = await self.http.download(attachment.url)

            if song is None:
                return await ctx.send("Couldn't download the song! I think it's Discord's fault!!")

            stream = (
                ffmpeg
                    .input("pipe:", format=f"{extension[1::]}")
                    .audio
                    .filter("atempo", 1.06)
                    .filter("asetrate", 44100 * 1.25)
                    .output("pipe:", format="mp3")
                    .get_args()
            )

            process = subprocess.Popen(
                ["ffmpeg"] + stream,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE
            )

            nightcored = BytesIO(process.communicate(input=song)[0])
            await ctx.send("どうぞ ^_^", file=discord.File(nightcored, filename))

        else:
            await ctx.send("You gotta upload a file!")

def setup(bot):
    bot.add_cog(Audio(bot))

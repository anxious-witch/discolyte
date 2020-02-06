import discord
import aiohttp
import ffmpeg
import subprocess
from io import BytesIO
from discord.ext import commands
from mimetypes import guess_extension

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

    async def __download(self, url: str):
        async with aiohttp.ClientSession(
            loop=self.bot.loop,
            connector=aiohttp.TCPConnector(verify_ssl=True)
        ) as session:
            async with session.head(url, timeout=10) as res:
                if res.status == 200:
                    extension_maybe = guess_extension(res.headers["Content-Type"])
                    if extension_maybe not in self.file_extension_whitelist:
                        return
                else:
                    return

            async with session.get(url, timeout=10) as res:
                return await res.read()

    @commands.command()
    async def nightcore(self, ctx):
        """ ONE TWO SEVEN THREE DOWN TO ROCKEFELLER STREET """
        if len(ctx.message.attachments) > 0:
            # Just get the first one for now
            attachment = ctx.message.attachments[0]
            filename = attachment.filename

            song = await self.__download(attachment.url)

            if song is None:
                return await ctx.send("Can't nightcore that! I read it in a book!!")

            stream = (
                ffmpeg
                    .input("pipe:", format="mp3")
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

def setup(bot):
    bot.add_cog(Audio(bot))

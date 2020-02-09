import discord
import ffmpeg
import subprocess
from io import BytesIO
from discord.ext import commands
from mimetypes import guess_extension

from acolyte.util.http import Http
from acolyte.util.fs import Filesystem


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
        self.fs = Filesystem()

    async def __get_extension(self, url: str):
        headers = await self.http.get_headers(url)

        if headers is not None:
            extension_maybe = guess_extension(headers["Content-Type"])
            if extension_maybe == ".oga":
                extension_maybe = ".ogg"

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

            path = self.fs.make_path(f"./assets/{filename}")
            song = await self.http.download(attachment.url)

            if song is None:
                return await ctx.send("Couldn't download the song! I think it's Discord's fault!!")

            await self.fs.write_binary_file(path, song)

            audio_input = (
                ffmpeg.input(path, format=f"{extension[1:]}")
                      .audio
                      .filter("atempo", 1.06)
                      .filter("asetrate", 44100 * 1.25)
            )
            video_input = ffmpeg.input(self.fs.get_random_file_path("./assets/cool_anime_pics"))

            stream = ffmpeg.output(audio_input, video_input, "pipe:", format="webm").get_args()
            process = subprocess.Popen(
                ["ffmpeg"] + ["-loglevel", "panic"] + stream,
                stdout=subprocess.PIPE
            )

            print(f"Generating nightcore for {ctx.author}...")

            nightcored = BytesIO(process.communicate(input=song)[0])
            filename = f"Nightcore - {filename}.webm"

            print("Done! Uploading...")

            self.fs.remove_file(path)

            await ctx.send(file=discord.File(nightcored, filename))
        else:
            await ctx.send("You gotta upload a file!")


def setup(bot):
    bot.add_cog(Audio(bot))

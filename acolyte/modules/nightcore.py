import discord
import ffmpeg
import subprocess
from io import BytesIO
from discord.ext import commands

from acolyte.util.http import Http
from acolyte.util.fs import Filesystem
from acolyte.util.magic import Magic

UPLOAD_LIMIT_IN_BYTES = 8388119


class Nightcore(commands.Cog):
    """ Post-avant jazzcore"""

    def __init__(self, bot):
        self.bot = bot
        self.http = Http(self.bot.session)
        self.fs = Filesystem()
        self.magic = Magic()


    @commands.group()
    async def nightcore(self, ctx):
        """ Nightcore commands! """
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid nightcore command!!")

    @nightcore.group()
    async def images(self, ctx):
        """ COOL ANIME PICS commands! """
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid images command!!")

    @nightcore.command()
    async def generate(self, ctx):
        """ ONE TWO SEVEN THREE DOWN TO ROCKEFELLER STREET """
        message = ctx.message

        if len(message.attachments) < 1:
            return await ctx.send("Hey I need a song!!")

        # Just get the first one for now
        attachment = message.attachments[0]

        filename = attachment.filename.split('.')[0]
        original_extension = attachment.filename.split('.')[-1]

        path = self.fs.make_path(f"./assets/{filename}")
        song = await self.http.download(attachment.url)
        extension = self.magic.get_audio_extension(song)

        if song is None:
            return await ctx.send("Couldn't download the song! I think it's Discord's fault!!")
        
        if extension is None and filename == original_extension:
            return await ctx.send(
                "What the HECK is this, I don't think this is an audio file??? listen i might be wrong about this"
            )
        elif extension is None:
            # Just try to generate it with the original extension, it might work!
            extension = original_extension
            await message.add_reaction('\N{BLACK QUESTION MARK ORNAMENT}')
        else:
            await message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

        await self.fs.write_binary_file(path, song)

        audio_input = (
            ffmpeg.input(path, format=extension)
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

        if nightcored.getbuffer().nbytes > UPLOAD_LIMIT_IN_BYTES:
            await ctx.send(":police_car: Waoow!! The video is TOO BIG for Discord!!! :police_car:")

        await ctx.send(file=discord.File(nightcored, filename))

    @images.command()
    async def add(self, ctx):
        """ Upload a COOL ANIME PIC """
        if len(ctx.message.attachments) != 1:
            return await ctx.send("Only one image per upload thanks bye!!")

        attachment = ctx.message.attachments[0]
        image = await self.http.download(attachment.url)
        extension = self.magic.get_image_extension(image)

        if extension is None:
            return await ctx.send("Hey! That's NOT a cool anime pic!!")

        filename = await self.fs.generate_filename(f".{extension}")

        path = self.fs.make_path(f"./assets/cool_anime_pics/{filename}")

        await self.fs.write_binary_file(path, image)
        await ctx.send(f"Cool pic!! Uploaded!!!")

    @images.command()
    async def list(self, ctx):
        ls = self.fs.get_directory_listing("./assets/cool_anime_pics")
        await ctx.send(ls)


def setup(bot):
    bot.add_cog(Nightcore(bot))

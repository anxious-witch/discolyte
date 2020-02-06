import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded
from discord.ext.commands.errors import ExtensionNotFound
from discord.ext.commands.errors import ExtensionNotLoaded

class Loader(commands.Cog):
    """ Module loader """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def load(self, ctx, *, extension_name):
        """ Load a module """
        try:
            self.bot.load_extension(f"modules.{extension_name}")
            self.bot.extensions.add(f"modules.{extension_name}")
            await ctx.send(f"Module {extension_name} loaded!!")
        except (AttributeError, ImportError):
            await ctx.send("Failed to load extension ;_;")
        except ExtensionNotFound:
            await ctx.send("No module found by that name! I looked everywhere!!")
        except ExtensionAlreadyLoaded:
            await ctx.send("WOA!! This module is already loaded!! :tada: :tada:")

    @commands.command(hidden=True)
    async def unload(self, ctx, *, extension_name):
        """ Unload a module """
        if extension_name == "loader":
            await ctx.send("hey don't")
            return

        try:
            self.bot.unload_extension(f"modules.{extension_name}")
            self.bot.extensions.remove(f"modules.{extension_name}")
            await ctx.send(f"Module {extension_name} unloaded!! Bye!!")
        except ExtensionNotLoaded:
            await ctx.send(f"Nope! This module isn't loaded!")

    @commands.command(hidden=True)
    async def reload(self, ctx):
        """ Reload all loaded modules """
        for ext in self.bot.extensions:
            self.bot.reload_extension(ext)
        await ctx.send(f"Reloaded {len(self.bot.extensions)} modules!!")

    @commands.command(hidden=True)
    async def list(self, ctx):
        """ List all loaded modules """
        await ctx.send(f"Loaded modules: {self.bot.extensions}")

def setup(bot):
    bot.add_cog(Loader(bot))

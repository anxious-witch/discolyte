from discord.ext import commands


class Chat(commands.Cog):
    """ Talk to Acolyte! """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """ Say hi! """
        await ctx.send("Hello!")


def setup(bot):
    bot.add_cog(Chat(bot))

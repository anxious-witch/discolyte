import discord
from discord.ext import commands

class Chat():
    """ Talk to Acolyte! """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self):
        await self.bot.say("Hello!")

    @commands.command()
    async def sucks(self):
        await self.bot.say("what the fuck did you just say to me binch? :gun: :eyes:")

    @commands.command()
    async def rocks(self):
        await self.bot.say(":blush:")

def setup(bot):
    bot.add_cog(Chat(bot))

import discord
from discord.ext import commands
import sys
import os

sys.path.insert(0, "..")

class Chat():
    """ Talk to Acolyte! """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self):
        """ Say hi! """ 
        await self.bot.say("Hello!")

def setup(bot):
    bot.add_cog(Chat(bot))

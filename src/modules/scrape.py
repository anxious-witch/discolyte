from utils import generate_filename
from discord.ext import commands
from utils import download
import urllib.parse
import discord
import utils
import sys
import os

sys.path.insert(0, "..")

async def latex_get(loop, equation):
    s = urllib.parse.quote_plus(equation)
    url = "https://chart.googleapis.com/chart?"
    parameters = {
        "cht":"tx", 
        "chl": equation,
        "chf": "bg,s,36393E",
        "chco": "EEEEEE"
    }
    return await download(loop, url, parameters)

class Scrape():
    def __init__(self, bot):
        self.bot = bot
        self.math = []

    @commands.command()
    async def latex(self, *equation : str):
        """ Parses LaTeX markup into a png via Google Charts 
            \\displaystyle is forced for nicer and bigger equations """
        equation = "\\displaystyle " + " ".join(equation)
        if equation == "": return
        res = await latex_get(self.bot.loop, equation)
        filename = generate_filename()
        with open(filename, "wb") as f:
            f.write(res)
        self.math.append(await self.bot.upload(filename))
        os.remove(filename)

    @commands.command()
    async def remove(self):
        """ Removes LaTeX images previously posted in the chat """
        while self.math:
            message = math.pop()
            await self.bot.delete_message(message)

def setup(bot):
    bot.add_cog(Scrape(bot))

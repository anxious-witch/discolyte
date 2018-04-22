import discord
from utils import generate_filename
from utils import convert_to_webm
from discord.ext import commands
from gtts import gTTS
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

    @commands.command()
    async def sucks(self):
        """ Don't push your luck..... """
        await self.bot.say("what the fuck did you just say to me binch? :gun: :eyes:")

    @commands.command()
    async def rocks(self):
        """ !!! """
        await self.bot.say(":blush:")

    @commands.command()
    async def tts(self, lang : str,  *message : str):
        """ Say something in text-to-speech 
            List of supported languages: 
                https://github.com/pndurette/gTTS#supported-languages
            Don't abuse this or I'll cry
        """
        languages = ['af','sq','ar','hy','bn','ca','zh','zh-cn','zh-tw','zh-yue','hr','cs','da','nl','en','en-au','en-uk','en-us','eo','fi','fr','de','el','hi','hu','is','id','it','ja','km','ko','la','lv','mk','no','pl','pt','ro','ru','sr','si','sk','es','es-es','es-us','sw','sv','ta','th','tr','uk','vi','cy']
        if lang not in languages:
            return
        s = "".join(message)
        if len(s) > 128:
            await self.bot.say("The character limit is 128, sorry! :bow: ")
        filename = generate_filename(".mp3")
        tts = gTTS(text="".join(message), lang=lang)
        tts.save(filename)
        speech = convert_to_webm(filename)
        await self.bot.upload(speech)
        os.remove(speech)

def setup(bot):
    bot.add_cog(Chat(bot))

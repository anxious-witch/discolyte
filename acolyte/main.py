from discord.ext import commands
import discord
import asyncio
import secret
import scrape
import misc
import os

description = "Hi! I'm Acolyte. I'm not the smartest nor the quickest, but I do my best!"

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
client = discord.Client()

math_messages = []
initial_extensions = [
    "modules.random",
    "modules.chat"
]

@bot.event
async def on_ready():
    print("Logged in!")
    print("Username: " + bot.user.name)
    print("User ID:  " + bot.user.id)

@bot.command()
async def latex(*equation : str):
    """ Parses LaTeX markup into a png via Google Charts 
        \\displaystyle is forced for nicer and bigger equations """
    equation = "\\displaystyle" + " ".join(equation)
    if equation == "": return
    res = await scrape.latex_get(bot.loop, equation)
    filename = misc.generate_filename()
    with open(filename, "wb") as f:
        f.write(res)
    math_messages.append(await bot.upload(filename))
    os.remove(filename)

@bot.command()
async def remove():
    """ Removes LaTeX images when you feel the bot is shitting up the chat """
    while math_messages:
        message = math_messages.pop()
        await bot.delete_message(message)

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except (AttributeError, ImportError) as oops:
            print("Failed to load extension!")
            print("{}: {}".format(type(oops), str(oops)))
bot.run(secret.token)

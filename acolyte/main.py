from discord.ext import commands
import discord
import asyncio
import secret

description = "Hi! I'm Acolyte. I'm not the smartest nor the quickest, but I do my best!"

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
client = discord.Client()

initial_extensions = [
    "modules.random",
    "modules.scrape",
    "modules.chat"
]

@bot.event
async def on_ready():
    print("Logged in!")
    print("Username: " + bot.user.name)
    print("User ID:  " + bot.user.id)

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except (AttributeError, ImportError) as oops:
            print("Failed to load extension!")
            print("{}: {}".format(type(oops), str(oops)))

bot.run(secret.token)

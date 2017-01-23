from discord.ext import commands
import chatcommands
import discord
import asyncio
import secret
import scrape
import misc
import os

description = "A buggy piece of shit lazily hacked together by a magician"

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
client = discord.Client()

meme_messages = []
math_messages = []

@bot.event
async def on_ready():
    print("Logged in")
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def hello():
    await bot.say("Hello!")

@bot.command()
async def sucks():
    await bot.say("what the fuck did you just say to me binch? :gun: :eyes:")

@bot.command()
async def latex(*equation : str):
    """ Parses LaTeX markup into a png via Google Charts
        Keep in mind that the parser is running in math mode
        Use $$ $$ or \displaystyle for nicer (bigger) formulae """
    equation = " ".join(equation)
    if equation == "": return
    res = await scrape.latex_get(bot.loop, equation)
    filename = misc.generate_filename()
    with open(filename, "wb") as f:
        f.write(res)
    math_messages.append(await bot.upload(filename))
    os.remove(filename)

@bot.command()
async def roll(dice : str):
    """ Roll n die of d sides 
        Example: roll 4d6 """
    try:
        n, d = [int(x) for x in dice.split("d")]
        # I feel that this is reasonable enough for any serious dice rolls...
        if n <= 100 and 1000 >= d >= 1:
            await bot.say("Rolling {}d{}! :game_die:".format(n, d))
            await bot.say("`{}`".format(chatcommands.roll(n, d)))
        else:
            await bot.say("Whoa there buddy, keep it reasonable :eyes:")
    except ValueError:
        await bot.say("Invalid syntax! :anger: `!roll 1d20`")

@bot.command()
async def emojipasta(pasta = "random"):
    """ Responds with a emojipasta - why did I make this """
    meme_messages.append(await bot.say(chatcommands.emojipasta(pasta)))

@bot.command()
async def remove(selection : str):
    """ Removes messages when you feel the bot is shitting up the chat 
        [remove meme] deletes all the emojipasta messages
        [remove math] deletes all the LaTeX images posted """
    if selection == "meme":
        while meme_messages:
            message = meme_messages.pop()
            await bot.delete_message(message)

    if selection == "math":
        while math_messages:
            message = math_messages.pop()
            await bot.delete_message(message)

bot.run(secret.token)

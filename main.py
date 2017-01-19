from discord.ext import commands
import chatcommands
import discord
import asyncio
import secret
import memes

description = "A badly written bot"

bot = commands.Bot(command_prefix="!", description=description)
bad_messages = []

@bot.event
async def on_ready():
    print("Logged in")
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def hello():
    await bot.say("Hello!")

@bot.command()
async def latex():
    await bot.say("Coming soon! :tm:")

@bot.command()
async def roll(dice : str):
    """ Roll 1 - 100 (inclusive) die of 1 - 1000 (inclusive) sides
        Returns each individual roll and the sum of the rolls """
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
    bad_messages.append(await bot.say(chatcommands.emojipasta(pasta)))

@bot.command()
async def remove(selection : str):
    """ Deletes messages, right now it only has one case - the horrible emojipasta """
    if selection == "meme":
        await bot.say(bad_messages)
        while bad_messages:
            message = bad_messages.pop()
            await bot.delete_message(message)
        await bot.say("Order has been restored :blush:")

bot.run(secret.token)

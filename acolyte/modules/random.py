import discord
from random import randint
from datetime import datetime
from discord.ext import commands

def roll_dice(self, n, d):
    dsum = 0
    die = []
    for _ in range(n):
        i = randint(1, d)
        die.append(i)
        dsum += i
    s = ""
    for i, dice in enumerate(sorted(die)):
        if i == n-1:
            s += str(dice)
        else:
            s += str(dice) + " "
            if dice < 10: s += " "
            if dice < 100: s += " "
        if (i+1) % 10 == 0: 
            s += "\n"
    s = "The sum of the roll was {}! :eyes:\nHere are all the rolls...\n\n```\n{}```".format(dsum, s)
    return s

class Random():
    """ Cool stuff related to randomness """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice : str):
        """ Roll n die of d sides """
        try:
            n, d = [int(x) for x in dice.split("d")]
            # I feel that this is reasonable enough for any serious dice rolls...
            if n <= 100 and 1 <= d <= 100:
                rollmessage = discord.Embed(
                    title="Rolling {}d{}! :game_die:".format(n, d),
                    description=self.roll_dice(n, d),
                    color=discord.Colour.green())
            else:
                rollmessage = discord.Embed(
                    title="Whoa there buddy :eyes:",
                    description="Keep your rolls reasonable.\n \
                    100 or fewer die with 100 or fewer sides!",
                    color=discord.Colour.red())
                rollmessage.set_footer(text="that's enough, right?")
            await self.bot.say(embed=rollmessage)
        except ValueError:
            error = discord.Embed(
                title="Invalid syntax! :anger:", 
                description="Here's how you use it.\n`@Acolyte roll 1d20`",
                colour=discord.Colour.red())
            error.set_footer(text="stupid dingus...")
            await self.bot.say(embed=error)
    @commands.command()
    async def eightball(self, *question : str):
        """ Ask the prophet a question! """
        answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]
        prophecy = discord.Embed(
            title="Consulting the crystal ball... :crystal_ball: :mag: :eyes:",
            description="The prophet says... {}".format(answers[randint(0, len(answers)-1)].lower()),
            colour=discord.Colour.purple())
        await self.bot.say(embed=prophecy)

def setup(bot):
    bot.add_cog(Random(bot))

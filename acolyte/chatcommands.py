from random import randint
import discord

def roll(n, d):
    # Roll an n number for d sided die
    rollingsum = 0
    if n > 1:
        i = randint(1, d) 
        rollingsum += i
        s = "{}".format(i)
        for _ in range(n - 1):
            i = randint(1, d)
            s += " + {}".format(i)
            rollingsum += i
        s += " = {}".format(rollingsum)
        return s
    else:
        i = randint(1, d)
        s = "{}".format(i)
        return s

def embed(tit, desc, foot, uri = None, col = discord.Colour.blue()):
    message = discord.Embed(title=tit, description = desc, colour=col)
    message.set_thumbnail(url="https://avatars1.githubusercontent.com/u/8780295?v=3&s=460")
    message.set_author(name="Acolyte")
    message.set_footer(text=foot)

    return message

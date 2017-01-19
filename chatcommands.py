from random import randint
import memes

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

def emojipasta(pasta):
    # Why did I make this?
    if pasta == "random":
        pasta = list(memes.emoji.keys())[randint(0, len(memes.emoji) - 1)]
    try:
        return memes.emoji[pasta]
    except KeyError:
        return memes.no

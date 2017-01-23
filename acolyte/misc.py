from random import randint
import string

""" A series of miscellaneous functions
    Name generation functions and things
    of that nature will go in here """

def generate_filename(extension=".png"):
    s = ""
    l = len(string.hexdigits) - 1
    for _ in range(12):
        s += string.hexdigits[randint(0, l)]
    return s + extension

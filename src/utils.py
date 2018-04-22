from random import randint
import async_timeout
import subprocess
import aiohttp
import string
import os

def generate_filename(extension=".png"):
    s = ""
    l = len(string.hexdigits) - 1
    for _ in range(12):
        s += string.hexdigits[randint(0, l)]
    return s + extension

def convert_to_webm(filename):
    new_file = filename.split('.')[0] + ".webm"
    cmd = ["/cygdrive/c/Users/magician/Downloads/trackers/ffmpeg.exe", "-loop", "1", 
           "-i", "image.jpg", "-i", filename, "-shortest", 
           #"-filter:a", "rubberband=tempo=0.3,pitch=0.5",
           #new_file]

           #"-filter:a", "atempo=0.5, atempo=0.5, atempo=0.7, chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3, volume=10", new_file]
           "-filter:a", "atempo=0.5, atempo=0.5, atempo=0.7, volume=20" new_file]

    subprocess.Popen(cmd).wait()
    os.remove(filename)
    return new_file

async def download(loop, url, parameters={}):
    # A semi-generic download function, might need some tweaking later on
    async with aiohttp.ClientSession(loop=loop) as session:
        with async_timeout.timeout(10):
            async with session.get(url, params=parameters) as resp:
                return await resp.read()


# Acolyte
A small and simple little Discord bot written in Python that utilizes the [discord.py](https://github.com/Rapptz/discord.py) library.

### Setup

The bot is written in Python 3.8.1 and the environment is set up for it.

This project uses pipenv to manage dependencies. Get pipenv with `pip install pipenv`

1. Clone the repo and run `pipenv install` in the project root.
2. Spawn a shell with `pipenv shell`
3. Create an `.env` file from the `.env.example`
4. Run `python -m acolyte` to start the bot.


### Extra setup

The audio module depends on ffmpeg in your PATH for some commands. Make sure it's installed and in your PATH or unload the module by editing the `__main__.py` file.


The nightcore has the extra caveat that it has to have the folder `cool_anime_pics` under the assets folder, that contains COOL ANIME PICS for generating a nightcore music video. It'll probably break if there isn't one in there.


### Hack away

Most reusable methods are kept under the `./acolyte/util` folder. Acolyte is set up as a Python module, so you can import with absolute paths anywhere. E.g. `from acolyte.util.fs import Filesystem`


Flake8 is used for PEP8 code style rules. The max line length is increased to 119 lines though.

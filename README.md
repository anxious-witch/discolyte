![Acolint](https://github.com/anxious-witch/acolyte/workflows/Acolint/badge.svg?branch=master&event=push)

# Acolyte

A small and simple little Discord bot written in Python that utilizes the [discord.py](https://github.com/Rapptz/discord.py) library.

### Dependencies

The bot depends on Python 3.9 and uses [poetry](https://python-poetry.org/) to manage dependencies.

libmagic is used for file type detection and the audio module depends on ffmpeg. Make sure you have libmagic installed and ffmpeg both installed and in your `$PATH`.

### Setup

1. Clone the repo and run `poetry shell` to create a virtual environment and spawn a shell
2. Install dependencies with `poetry install`
3. Create an `.env` file from the `.env.example`
4. Run `python -m acolyte` to start the bot.

### Hack away

Most reusable methods are kept under the `./acolyte/util` folder. Acolyte is set up as a Python module, so you can import with absolute paths anywhere. E.g. `from acolyte.util.fs import Filesystem`

Running the bot with `ACOLYTE_ENV` set to development runs a filesystem observer that automatically reload everything under `/modules` on change. Note that the reload is not atomic.

Flake8 is used for PEP8 code style rules. The max line length is increased to 119 lines though.

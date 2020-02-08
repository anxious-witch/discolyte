from acolyte import Acolyte
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    acolyte = Acolyte(os.getenv("BOT_TOKEN"))

    acolyte.run()

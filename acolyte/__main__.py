from acolyte import Acolyte
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    dev = True if os.getenv("ACOLYTE_ENV") == "development" else False

    acolyte = Acolyte(
        os.getenv("ACOLYTE_TOKEN"),
        development=dev
    )

    acolyte.run()

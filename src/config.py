from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "televault")


def validate():
    if not API_ID:
        raise ValueError("API_ID is missing in .env")

    if not API_HASH:
        raise ValueError("API_HASH is missing in .env")

from telethon import TelegramClient

from src.config import API_ID, API_HASH, SESSION_NAME

client = TelegramClient(
    SESSION_NAME,
    int(API_ID),
    API_HASH,
)

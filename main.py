import asyncio

import typer

from src.client import client
from src.config import validate
from src.commands.list import list_chats as list_chats_cmd
from src.commands.archive import archive_chat

app = typer.Typer(
    help="TeleVault - Archive your Telegram chats."
)


@app.command()
def list():
    """List Telegram chats."""

    async def runner():
        validate()
        await client.start()
        await list_chats_cmd(client)
        await client.disconnect()

    asyncio.run(runner())

@app.command()
def archive(chat: str):
    """Archive a Telegram chat."""

    asyncio.run(archive_chat(chat))

if __name__ == "__main__":
    app()


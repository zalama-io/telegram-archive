from pathlib import Path

from rich.console import Console

from src.client import client
from src.config import validate
from src.services.archive_service import save_messages
from src.services.media_service import download_media
from src.services.serializer import serialize_message

console = Console()


async def archive_chat(chat: str):
    validate()

    await client.start()

    entity = await client.get_entity(chat)

    chat_name = (
        getattr(entity, "username", None)
        or getattr(entity, "title", None)
        or str(entity.id)
    )

    console.print(f"[green]Archiving:[/green] {chat_name}")

    media_dir = Path("archive") / chat_name / "media"

    data = []

    async for message in client.iter_messages(entity, limit=10):
        media_path = await download_media(client, message, media_dir)

        data.append(
            serialize_message(
                message,
                media_path=media_path,
            )
        )

    save_messages(chat_name, data)

    console.print(f"[bold green]✓ Archived {len(data)} messages[/bold green]")

    await client.disconnect()

from rich.console import Console

from src.client import client
from src.config import validate
from src.services.archive_service import save_messages

console = Console()


async def archive_chat(chat: str):
    validate()

    await client.start()

    entity = await client.get_entity(chat)

    console.print(f"[green]Archiving:[/green] {getattr(entity, 'title', chat)}")

    messages = []

    async for message in client.iter_messages(entity, limit=100):
        messages.append(message)

    chat_name = (
        getattr(entity, "username", None)
        or getattr(entity, "title", None)
        or str(entity.id)
    )

    save_messages(chat_name, messages)

    console.print(f"[bold green]✓ Saved {len(messages)} messages[/bold green]")

    await client.disconnect()

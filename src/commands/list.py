from rich.console import Console
from rich.table import Table

console = Console()


async def list_chats(client):
    table = Table(title="Telegram Chats")

    table.add_column("#", justify="right", style="cyan")
    table.add_column("ID", style="magenta")
    table.add_column("Name", style="green")
    table.add_column("Type", style="yellow")

    index = 1

    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            chat_type = "Channel"
        elif dialog.is_group:
            chat_type = "Group"
        else:
            chat_type = "Private"

        table.add_row(
            str(index),
            str(dialog.id),
            dialog.name,
            chat_type,
        )

        index += 1

    console.print(table)

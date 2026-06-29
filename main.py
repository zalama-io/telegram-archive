import asyncio

from rich.console import Console
from rich.panel import Panel

from src.client import client
from src.config import validate

console = Console()


async def main():
    validate()

    await client.start()

    me = await client.get_me()

    console.print(
        Panel.fit(
            f"[bold green]Welcome[/bold green]\n\n"
            f"Name : {me.first_name}\n"
            f"Username : @{me.username}",
            title="TeleVault",
        )
    )

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

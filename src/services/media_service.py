from pathlib import Path

from rich.console import Console

console = Console()


async def download_media(client, message, media_dir: Path):
    """
    Download media attached to a Telegram message.

    Returns:
        str | None: Downloaded file path or None.
    """

    if not message.media:
        return None

    media_dir.mkdir(parents=True, exist_ok=True)

    try:
        file_path = await client.download_media(
            message,
            file=str(media_dir),
        )
        return file_path

    except Exception as e:
        console.print(
            f"[yellow]Warning:[/yellow] Failed to download media "
            f"from message {message.id}: {e}"
        )
        return None

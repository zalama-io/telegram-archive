from telethon.tl.custom.message import Message


def serialize_message(message: Message, media_path: str | None = None) -> dict:
    return {
        "id": message.id,
        "date": message.date.isoformat() if message.date else None,
        "text": message.text or "",
        "views": getattr(message, "views", None),
        "media": message.media is not None,
        "media_path": media_path,
    }

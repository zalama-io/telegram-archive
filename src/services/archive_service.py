from pathlib import Path
import json

from telethon.tl.custom.message import Message


def save_messages(chat_name: str, messages: list[Message]):
    folder = Path("archive") / chat_name
    folder.mkdir(parents=True, exist_ok=True)

    data = []

    for message in messages:
        data.append(
            {
                "id": message.id,
                "date": message.date.isoformat() if message.date else None,
                "text": message.text,
                "views": getattr(message, "views", None),
            }
        )

    with open(folder / "messages.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

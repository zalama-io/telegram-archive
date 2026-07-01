from pathlib import Path
import json


def save_messages(chat_name: str, data: list[dict]):
    folder = Path("archive") / chat_name
    folder.mkdir(parents=True, exist_ok=True)

    with open(folder / "messages.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

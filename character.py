import json
import os

CHARACTER_FILE = "character.json"

def load_character() -> dict:
    if not os.path.isfile(CHARACTER_FILE):
        return {}

    with open(CHARACTER_FILE, "r", encoding="utf-8") as read_file:
        return json.load(read_file)


def save_character(character: dict) -> None:
    with open(CHARACTER_FILE, "w", encoding="utf-8") as write_file:
        json.dump(character, write_file, indent=4, ensure_ascii=False)


def show_info() -> dict:
    return load_character()
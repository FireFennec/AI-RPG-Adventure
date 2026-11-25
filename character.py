import json
import os

def show_info():
    character = {}

    if os.path.isfile('character.json'):
        with open('character.json', 'r', encoding="utf-8") as read_file:
            character = json.load(read_file)
        return character
    else:
        return character
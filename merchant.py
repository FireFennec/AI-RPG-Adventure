import json

def shop_list():
    items = [
        {
            "id": 1,
            "name": "wooden short sword",
            "price": 20
        },
        {
            "id": 2,
            "name": "simple bow",
            "price": 10
         },
        {
            "id": 3,
            "name": "wooden shield",
            "price": 10
         },
        {
            "id": 4,
            "name": "wooden great sword",
            "price": 35
        }
    ]

    return items

def buy_item(item_id):
    items = shop_list()

    for item in items:
        if item['id'] == item_id:

            with open('character.json', 'r', encoding='utf-8') as read_file:
                character = json.load(read_file)

            if item['price'] <= character['gold']:
                character['gold'] -= item['price']
                character['inventory'].append(item['name'])

                with open('character.json', 'w', encoding='utf-8') as write_file:
                    json.dump(character, write_file, indent=4, ensure_ascii=False)

                return {
                    "success": True,
                    "item": item["name"],
                    "price": item["price"],
                    "remaining_gold": character["gold"]
                }

            return 'Not enough gold.'

    return 'Item not found.'
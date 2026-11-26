from character import load_character, save_character

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
        if item["id"] == item_id:

            character = load_character()

            if not character:
                return {
                    "success": False,
                    "message": "Character data not found.",
                }

            if item["price"] <= character["gold"]:
                character["gold"] -= item["price"]
                character["inventory"].append(item["name"])

                save_character(character)

                return {
                    "success": True,
                    "item": item["name"],
                    "price": item["price"],
                    "remaining_gold": character["gold"]
                }

            return {
                "success": False,
                "message": "Not enough gold to purchase the item.",
            }

    return {
        "success": False,
        "message": "Item not found."
    }
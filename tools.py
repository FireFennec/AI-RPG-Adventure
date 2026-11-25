from openai.types.responses import FunctionToolParam

tools: list[FunctionToolParam] = [
    {
        "type": "function",
        "name": "shop_list",
        "description": "Shows the player the items available in the merchant's shop.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "show_character",
        "description": "Shows the player's character information, including name, level, gold and inventory.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "buy_item",
        "description": "Purchases an item using its unique ID from the shop catalog when the player clearly requests a purchase. Never guess an item ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "item_id": {
                    "type": "integer",
                    "description": "The unique ID of the item to purchase from the shop catalog."
                }
            },
            "required": ["item_id"],
            "additionalProperties": False
        },
        "strict": True
    }
]
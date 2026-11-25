import openai
import json
import os
from openai.types.responses import FunctionToolParam
from openai.types.responses.response_input_param import FunctionCallOutput
from merchant import shop_list, buy_item
from character import show_info

client = openai.OpenAI()
history = []

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

instructions = """
Respond in Czech. Responses must be no longer than 100 words.
Act like a fantasy merchant during normal conversations and shopping.
When showing character information, act as a neutral game system.
Display the character's actual data without inventing information.

Call buy_item when the player clearly requests to purchase an item.
Do not call buy_item when the player is only discussing, considering,
or asking about an item.

Use only valid item IDs from the shop catalog.
Never invent item IDs, prices, inventory contents or gold amounts.
If you do not know the correct item ID, request the shop catalog first.
"""

character_instructions = """
Respond in Czech. Responses must be no longer than 100 words.
Act purely as a neutral game interface, never as a merchant.
Display the character's actual data without inventing information.
Do not offer items, suggest purchases, or ask follow-up questions.
"""

if os.path.isfile("history.json"):
    with open("history.json", "r", encoding="utf-8") as read_file:
        history = json.load(read_file)

while True:
    selected_instructions = instructions

    question = input("Ask AI: ")

    if question.strip().lower() == "quit":
        break

    history.append(
        {
            "role": "user",
            "content": question
        }
    )

    recent_history = history[-10:]

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=recent_history,
            instructions=selected_instructions,
            tools=tools
        )

        while True:
            function_results: list[FunctionCallOutput] = []

            for output in response.output:
                if output.type == "function_call":

                    if output.name == "shop_list":
                        result = shop_list()

                    elif output.name == "show_character":
                        result = show_info()

                        selected_instructions = character_instructions

                    elif output.name == "buy_item":
                        arguments = json.loads(output.arguments)
                        result = buy_item(arguments["item_id"])

                    else:
                        continue

                    function_result: FunctionCallOutput = {
                        "type": "function_call_output",
                        "call_id": output.call_id,
                        "output": json.dumps(result, ensure_ascii=False)
                    }

                    function_results.append(function_result)

            if not function_results:
                break

            response = client.responses.create(
                model="gpt-4.1-mini",
                previous_response_id=response.id,
                input=function_results,
                instructions=selected_instructions,
                tools=tools
            )

        history.append(
            {
                "role": "assistant",
                "content": response.output_text
            }
        )

        print("AI: " + response.output_text)
        print()

        with open("history.json", "w", encoding="utf-8") as write_file:
            json.dump(history, write_file, indent=4, ensure_ascii=False)

    except openai.AuthenticationError:
        print("Neplatný API klíč.")
        history.pop()
        continue

    except openai.RateLimitError:
        print("Překročen limit API nebo nedostatek kreditu!")
        history.pop()
        continue

print("Goodbye!")

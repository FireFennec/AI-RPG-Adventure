import openai
import json
import os
from openai.types.responses.response_input_param import FunctionCallOutput
from merchant import shop_list, buy_item
from character import show_info
from tools import tools
from prompts import instructions, character_instructions

client = openai.OpenAI()
history = []

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

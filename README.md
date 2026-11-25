
# AI RPG Adventure

## About the Project

AI RPG Adventure is a personal learning project built with Python
and the OpenAI API. Its goal is to gradually develop an AI-powered
interactive RPG with persistent character progression, dynamic NPCs,
and increasingly complex game mechanics.

The project combines AI-generated interactions with traditional
game logic handled by Python.

## Current Features

- AI-powered fantasy merchant
- Natural language interactions
- OpenAI Function Calling
- Multiple tool calls within a single interaction
- Character profile and inventory
- Item purchasing and gold management
- Persistent character data using JSON
- Persistent conversation history
- Dynamic AI instruction switching
- Basic API error handling

## Technologies

- Python
- OpenAI API
- JSON
- Git and GitHub

## Project Structure

    AI-RPG-Adventure/
    ├── ai.py
    ├── tools.py
    ├── prompts.py
    ├── merchant.py
    ├── character.py
    ├── character.example.json
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Installation

### 1. Clone the repository

    git clone https://github.com/FireFennec/AI-RPG-Adventure.git
    cd AI-RPG-Adventure

### 2. Create a virtual environment

    python -m venv .venv

Activate it on Windows (PowerShell):

    .\.venv\Scripts\Activate.ps1

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Configure your OpenAI API key

Set your API key as an environment variable in PowerShell:

    $env:OPENAI_API_KEY = "your-api-key"

Never share or commit your API key.

### 5. Initialize character data

Create a local character file from the provided example:

    Copy-Item character.example.json character.json

### 6. Run the application

    python ai.py

The application currently communicates in Czech.
Type `quit` to exit.

## Future Development

- Item selling
- Advanced inventory management
- Experience and character leveling
- Equipment and character statistics
- Quest system
- Combat mechanics
- Dynamic NPC interactions
- Expanded game world
- Improved AI decision-making
- Automated testing

## Project Status

The project is in early development and is continuously evolving
as part of my journey into Python and AI application development.

## Author

FireFennec

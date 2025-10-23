# OpenAI Chatbot

A simple chatbot implementation using OpenAI Chat Completions API.

## Features

- 🤖 Chat with OpenAI GPT models
- 💬 Maintain complete conversation history
- 🔄 Support clearing conversation history
- 📝 View conversation records
- 🎯 Support custom system prompts
- ⚙️ Configurable to use different models
- ⚡ Use uv for fast dependency management

## Installation

### Prerequisites

Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or use Homebrew (macOS/Linux):
```bash
brew install uv
```

### Project Setup

1. Clone or download this project

2. Use uv to sync dependencies (automatically creates virtual environment):
```bash
uv sync
```

3. Set OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or pass the API key directly in the code.

## Usage

### Method 1: Run with uv (recommended)

```bash
uv run chatbot
```

Or run the script directly:
```bash
uv run python chatbot.py
```

### Method 2: Run traditionally

```bash
python chatbot.py
```

Then follow the prompts to enter messages and start a conversation.

### Method 3: Use in code

```python
from chatbot import ChatBot

# Create chatbot instance
bot = ChatBot()

# Start conversation
response = bot.chat("Hello!")
print(response)

# Continue conversation (maintains context)
response = bot.chat("What can you help me with?")
print(response)

# Clear conversation history
bot.clear_history()

# Use custom system prompt
response = bot.chat(
    "Introduce yourself",
    system_prompt="You are a professional Python programming assistant"
)
print(response)
```

## Advantages of using uv

- ⚡ **Extremely fast dependency installation**: 10-100x faster than pip
- 🔒 **Automatic dependency locking**: Generates `uv.lock` for reproducible builds
- 🎯 **Automatic virtual environment management**: No need to manually create and activate virtual environments
- 📦 **Unified project management**: All configuration in `pyproject.toml`
- 🚀 **One-click execution**: `uv run` automatically handles environment setup

### Command Instructions

In interactive mode, you can use the following commands:

- Enter any text: Send message to AI
- `quit` or `exit`: Exit the program
- `clear`: Clear conversation history
- `history`: View complete conversation history

## Configuration Options

When creating a ChatBot instance, you can pass the following parameters:

- `api_key`: OpenAI API key (optional, defaults to reading from environment variable)
- `model`: Model name to use (defaults to "gpt-3.5-turbo")

Example:
```python
bot = ChatBot(api_key="your-key", model="gpt-4")
```

## Supported Models

- gpt-3.5-turbo (default, fast and cost-effective)
- gpt-4 (more powerful but higher cost)
- gpt-4-turbo
- Other OpenAI chat models

## Common uv Commands

```bash
# Sync/install dependencies
uv sync

# Add new dependency
uv add package-name

# Remove dependency
uv remove package-name

# Run script
uv run python chatbot.py

# Run defined command (defined in pyproject.toml)
uv run chatbot

# Update dependencies
uv lock --upgrade
```

## Notes

- Requires a valid OpenAI API key
- API calls incur charges
- Conversation history consumes tokens, clear regularly
- Network connection must be able to access OpenAI API

## License

MIT License

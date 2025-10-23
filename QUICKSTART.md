# Running OpenAI Chatbot with uv

## Quick Start

### 1. Install uv (if not already installed)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use Homebrew
brew install uv
```

### 2. Sync dependencies
```bash
cd /Users/sam/workspace/python/py2rs
uv sync
```

### 3. Set API Key
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### 4. Run the chatbot

**Method 1: Use project-defined command**
```bash
uv run chatbot
```

**Method 2: Run Python script directly**
```bash
uv run python chatbot.py
```

**Method 3: Run tests**
```bash
uv run python test_chatbot.py
```

## Advantages of uv over traditional methods

### Speed Comparison
- **Traditional method**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt  # May take 30-60 seconds
  python chatbot.py
  ```

- **uv method**:
  ```bash
  uv sync  # Only takes 1-2 seconds!
  uv run chatbot
  ```

### Main Advantages

1. **⚡ Extremely fast speed**: Install dependencies 10-100x faster than pip
2. **🔒 Dependency locking**: Automatically generates `uv.lock` file for environment consistency
3. **🎯 Automatic environment management**: No need to manually create/activate virtual environments
4. **📦 Unified configuration**: All configuration in `pyproject.toml`
5. **🚀 One-click execution**: `uv run` automatically handles environment setup

## Common uv Commands

```bash
# Install/sync dependencies
uv sync

# Add new dependency
uv add requests

# Remove dependency
uv remove requests

# Update all dependencies
uv lock --upgrade

# Run script
uv run python script.py

# Run project command (defined in pyproject.toml)
uv run chatbot

# List installed packages
uv pip list

# View project information
uv tree
```

## Project Structure

```
py2rs/
├── chatbot.py           # Main chatbot code
├── test_chatbot.py      # Test script
├── pyproject.toml       # Project configuration (used by uv)
├── requirements.txt     # Traditional pip dependency file
├── README.md           # Project documentation
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore file
└── .venv/              # Virtual environment (created automatically by uv)
```

## Troubleshooting

### Issue: uv command not found
**Solution**: Ensure uv is properly installed and in PATH
```bash
which uv
# If no output, reinstall uv
```

### Issue: Dependency installation failed
**Solution**: Clean cache and resync
```bash
uv cache clean
uv sync
```

### Issue: API key error
**Solution**: Ensure environment variable is set correctly
```bash
echo $OPENAI_API_KEY  # Check if set
export OPENAI_API_KEY='your-key-here'
```

## Next Steps

1. Get OpenAI API key: https://platform.openai.com/api-keys
2. Set environment variable
3. Run `uv run chatbot` to start chatting!

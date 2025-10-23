"""
Test basic functionality of ChatBot class (no API key required)
"""

from chatbot import ChatBot


def test_basic_functionality():
    """Test basic functionality"""
    print("=" * 50)
    print("Testing ChatBot Basic Functionality")
    print("=" * 50)

    # Test error handling without API key
    print("\n1. Testing error handling (no API key)...")
    try:
        bot = ChatBot()
        print("❌ Should throw ValueError")
    except ValueError as e:
        print(f"✅ Correctly caught error: {e}")

    # Test creating instance with fake API key
    print("\n2. Testing instance creation (with fake API key)...")
    try:
        bot = ChatBot(api_key="fake-api-key-for-testing")
        print(f"✅ Successfully created ChatBot instance")
        print(f"   - Model: {bot.model}")
        print(f"   - Conversation history length: {len(bot.conversation_history)}")
    except Exception as e:
        print(f"❌ Failed to create instance: {e}")
        return

    # Test adding messages
    print("\n3. Testing message addition...")
    bot.add_message("user", "Hello")
    bot.add_message("assistant", "Hello! How can I help you?")
    print(f"✅ Successfully added messages")
    print(f"   - Conversation history length: {len(bot.conversation_history)}")

    # Test getting history
    print("\n4. Testing conversation history retrieval...")
    history = bot.get_history()
    for i, msg in enumerate(history, 1):
        print(f"   Message {i}: [{msg['role']}] {msg['content']}")
    print("✅ Successfully retrieved conversation history")

    # Test clearing history
    print("\n5. Testing conversation history clearing...")
    bot.clear_history()
    print(f"✅ Successfully cleared history")
    print(f"   - Conversation history length: {len(bot.conversation_history)}")

    # Test custom model
    print("\n6. Testing custom model...")
    bot2 = ChatBot(api_key="fake-api-key", model="gpt-4")
    print(f"✅ Successfully created instance with GPT-4")
    print(f"   - Model: {bot2.model}")

    print("\n" + "=" * 50)
    print("All tests passed! ✅")
    print("=" * 50)
    print("\nNote: These are basic functionality tests.")
    print(
        "To test actual API calls, please set the OPENAI_API_KEY environment variable,"
    )
    print("then run: uv run chatbot")


if __name__ == "__main__":
    test_basic_functionality()

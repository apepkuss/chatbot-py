"""
OpenAI Chatbot - A chatbot implementation using OpenAI Chat Completions API
"""

import os

from openai import OpenAI


class ChatBot:
    """Chatbot class"""

    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """
        Initialize the chatbot

        Args:
            api_key: OpenAI API key, if None, read from environment variable OPENAI_API_KEY
            model: Model name to use, defaults to gpt-3.5-turbo
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Please provide OpenAI API key or set environment variable OPENAI_API_KEY"
            )

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.conversation_history = []

    def add_message(self, role, content):
        """
        Add message to conversation history

        Args:
            role: Message role (system/user/assistant)
            content: Message content
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def chat(self, user_input, system_prompt=None):
        """
        Send user message and get AI response

        Args:
            user_input: User input message
            system_prompt: System prompt (optional)

        Returns:
            AI response content
        """
        # If system prompt is provided and conversation history is empty, add system message
        if system_prompt and not self.conversation_history:
            self.add_message("system", system_prompt)

        # Add user message
        self.add_message("user", user_input)

        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history
            )

            # Get AI response
            assistant_message = response.choices[0].message.content

            # Add AI response to conversation history
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            return f"Error: {str(e)}"

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

    def get_history(self):
        """Get conversation history"""
        return self.conversation_history


def main():
    """Main function - Run interactive chat"""
    print("=" * 50)
    print("OpenAI Chatbot")
    print("=" * 50)
    print("Tips:")
    print("  - Enter message to start conversation")
    print("  - Enter 'quit' or 'exit' to quit")
    print("  - Enter 'clear' to clear conversation history")
    print("  - Enter 'history' to view conversation history")
    print("=" * 50)

    # Create chatbot instance
    try:
        chatbot = ChatBot()
    except ValueError as e:
        print(f"\nError: {e}")
        print("\nPlease set environment variable: export OPENAI_API_KEY='your-api-key'")
        return

    # Optional: Set system prompt
    system_prompt = "You are a friendly and helpful AI assistant."

    # Interactive conversation loop
    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            # Exit command
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("\nGoodbye!")
                break

            # Clear history command
            if user_input.lower() in ['clear', '清除']:
                chatbot.clear_history()
                print("\nConversation history cleared.")
                continue

            # View history command
            if user_input.lower() in ['history', '历史']:
                history = chatbot.get_history()
                if not history:
                    print("\nConversation history is empty.")
                else:
                    print("\nConversation history:")
                    for msg in history:
                        role = msg['role']
                        content = msg['content']
                        print(f"  [{role}]: {content}")
                continue

            # Send message and get response
            response = chatbot.chat(user_input, system_prompt)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
    main()

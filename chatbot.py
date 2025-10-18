"""
OpenAI Chatbot - 使用 OpenAI Chat Completions API 实现的聊天机器人
"""
import os

from openai import OpenAI


class ChatBot:
    """聊天机器人类"""

    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """
        初始化聊天机器人

        Args:
            api_key: OpenAI API密钥，如果为None则从环境变量OPENAI_API_KEY读取
            model: 使用的模型名称，默认为gpt-3.5-turbo
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("请提供OpenAI API密钥或设置环境变量OPENAI_API_KEY")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.conversation_history = []

    def add_message(self, role, content):
        """
        添加消息到对话历史

        Args:
            role: 消息角色 (system/user/assistant)
            content: 消息内容
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def chat(self, user_input, system_prompt=None):
        """
        发送用户消息并获取AI回复

        Args:
            user_input: 用户输入的消息
            system_prompt: 系统提示词（可选）

        Returns:
            AI的回复内容
        """
        # 如果提供了系统提示词且对话历史为空，则添加系统消息
        if system_prompt and not self.conversation_history:
            self.add_message("system", system_prompt)

        # 添加用户消息
        self.add_message("user", user_input)

        try:
            # 调用OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history
            )

            # 获取AI回复
            assistant_message = response.choices[0].message.content

            # 将AI回复添加到对话历史
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            return f"错误: {str(e)}"

    def clear_history(self):
        """清除对话历史"""
        self.conversation_history = []

    def get_history(self):
        """获取对话历史"""
        return self.conversation_history


def main():
    """主函数 - 运行交互式聊天"""
    print("=" * 50)
    print("OpenAI 聊天机器人")
    print("=" * 50)
    print("提示:")
    print("  - 输入消息开始对话")
    print("  - 输入 'quit' 或 'exit' 退出")
    print("  - 输入 'clear' 清除对话历史")
    print("  - 输入 'history' 查看对话历史")
    print("=" * 50)

    # 创建聊天机器人实例
    try:
        chatbot = ChatBot()
    except ValueError as e:
        print(f"\n错误: {e}")
        print("\n请设置环境变量: export OPENAI_API_KEY='your-api-key'")
        return

    # 可选：设置系统提示词
    system_prompt = "你是一个友好且乐于助人的AI助手。"

    # 交互式对话循环
    while True:
        try:
            user_input = input("\n你: ").strip()

            if not user_input:
                continue

            # 退出命令
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("\n再见！")
                break

            # 清除历史命令
            if user_input.lower() in ['clear', '清除']:
                chatbot.clear_history()
                print("\n对话历史已清除。")
                continue

            # 查看历史命令
            if user_input.lower() in ['history', '历史']:
                history = chatbot.get_history()
                if not history:
                    print("\n对话历史为空。")
                else:
                    print("\n对话历史:")
                    for msg in history:
                        role = msg['role']
                        content = msg['content']
                        print(f"  [{role}]: {content}")
                continue

            # 发送消息并获取回复
            response = chatbot.chat(user_input, system_prompt)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n发生错误: {e}")


if __name__ == "__main__":
    main()
    main()

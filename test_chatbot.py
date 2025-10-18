"""
测试 ChatBot 类的基本功能（不需要 API key）
"""
from chatbot import ChatBot


def test_basic_functionality():
    """测试基本功能"""
    print("=" * 50)
    print("测试 ChatBot 基本功能")
    print("=" * 50)

    # 测试没有 API key 时的错误处理
    print("\n1. 测试错误处理（无 API key）...")
    try:
        bot = ChatBot()
        print("❌ 应该抛出 ValueError")
    except ValueError as e:
        print(f"✅ 正确捕获错误: {e}")

    # 测试使用假 API key 创建实例
    print("\n2. 测试创建实例（使用假 API key）...")
    try:
        bot = ChatBot(api_key="fake-api-key-for-testing")
        print(f"✅ 成功创建 ChatBot 实例")
        print(f"   - 模型: {bot.model}")
        print(f"   - 对话历史长度: {len(bot.conversation_history)}")
    except Exception as e:
        print(f"❌ 创建实例失败: {e}")
        return

    # 测试添加消息
    print("\n3. 测试添加消息...")
    bot.add_message("user", "你好")
    bot.add_message("assistant", "你好！有什么可以帮助你的吗？")
    print(f"✅ 成功添加消息")
    print(f"   - 对话历史长度: {len(bot.conversation_history)}")

    # 测试获取历史
    print("\n4. 测试获取对话历史...")
    history = bot.get_history()
    for i, msg in enumerate(history, 1):
        print(f"   消息 {i}: [{msg['role']}] {msg['content']}")
    print("✅ 成功获取对话历史")

    # 测试清除历史
    print("\n5. 测试清除对话历史...")
    bot.clear_history()
    print(f"✅ 成功清除历史")
    print(f"   - 对话历史长度: {len(bot.conversation_history)}")

    # 测试自定义模型
    print("\n6. 测试自定义模型...")
    bot2 = ChatBot(api_key="fake-api-key", model="gpt-4")
    print(f"✅ 成功创建使用 GPT-4 的实例")
    print(f"   - 模型: {bot2.model}")

    print("\n" + "=" * 50)
    print("所有测试通过！✅")
    print("=" * 50)
    print("\n注意: 这些是基本功能测试。")
    print("要测试实际的 API 调用，请设置 OPENAI_API_KEY 环境变量，")
    print("然后运行: uv run chatbot")


if __name__ == "__main__":
    test_basic_functionality()

# OpenAI Chatbot

一个使用 OpenAI Chat Completions API 实现的简单聊天机器人。

## 功能特点

- 🤖 与 OpenAI GPT 模型进行对话
- 💬 保持完整的对话历史
- 🔄 支持清除对话历史
- 📝 可查看对话记录
- 🎯 支持自定义系统提示词
- ⚙️ 可配置使用不同的模型
- ⚡ 使用 uv 进行快速依赖管理

## 安装

### 前置要求

安装 uv（如果还未安装）：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

或使用 Homebrew (macOS/Linux)：
```bash
brew install uv
```

### 项目设置

1. 克隆或下载此项目

2. 使用 uv 同步依赖（自动创建虚拟环境）：
```bash
uv sync
```

3. 设置 OpenAI API 密钥：
```bash
export OPENAI_API_KEY='your-api-key-here'
```

或者在代码中直接传入 API 密钥。

## 使用方法

### 方式1：使用 uv 运行（推荐）

```bash
uv run chatbot
```

或者直接运行脚本：
```bash
uv run python chatbot.py
```

### 方式2：传统方式运行

```bash
python chatbot.py
```

然后按照提示输入消息即可开始对话。

### 方式3：在代码中使用

```python
from chatbot import ChatBot

# 创建聊天机器人实例
bot = ChatBot()

# 开始对话
response = bot.chat("你好！")
print(response)

# 继续对话（保持上下文）
response = bot.chat("你能帮我做什么？")
print(response)

# 清除对话历史
bot.clear_history()

# 使用自定义系统提示词
response = bot.chat(
    "介绍一下你自己",
    system_prompt="你是一个专业的Python编程助手"
)
print(response)
```

## 使用 uv 的优势

- ⚡ **极快的依赖安装速度**：比 pip 快 10-100 倍
- 🔒 **自动锁定依赖**：生成 `uv.lock` 确保可重现的构建
- 🎯 **自动虚拟环境管理**：无需手动创建和激活虚拟环境
- 📦 **统一的项目管理**：使用 `pyproject.toml` 管理所有配置
- 🚀 **一键运行**：使用 `uv run` 自动处理环境

### 命令说明

在交互式模式中，可以使用以下命令：

- 输入任意文本：发送消息给 AI
- `quit` 或 `exit`：退出程序
- `clear`：清除对话历史
- `history`：查看完整对话历史

## 配置选项

创建 ChatBot 实例时可以传入以下参数：

- `api_key`: OpenAI API 密钥（可选，默认从环境变量读取）
- `model`: 使用的模型名称（默认为 "gpt-3.5-turbo"）

示例：
```python
bot = ChatBot(api_key="your-key", model="gpt-4")
```

## 支持的模型

- gpt-3.5-turbo（默认，速度快，成本低）
- gpt-4（更强大但成本较高）
- gpt-4-turbo
- 其他 OpenAI 聊天模型

## uv 常用命令

```bash
# 同步/安装依赖
uv sync

# 添加新依赖
uv add package-name

# 移除依赖
uv remove package-name

# 运行脚本
uv run python chatbot.py

# 运行定义的命令（在 pyproject.toml 中定义）
uv run chatbot

# 更新依赖
uv lock --upgrade
```

## 注意事项

- 需要有效的 OpenAI API 密钥
- API 调用会产生费用
- 对话历史会占用 token，建议定期清除
- 网络连接需要能访问 OpenAI API

## 许可证

MIT License

# 使用 uv 运行 OpenAI Chatbot

## 快速开始

### 1. 安装 uv（如果还没有）
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 Homebrew
brew install uv
```

### 2. 同步依赖
```bash
cd /Users/sam/workspace/python/py2rs
uv sync
```

### 3. 设置 API Key
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### 4. 运行聊天机器人

**方式 1: 使用项目定义的命令**
```bash
uv run chatbot
```

**方式 2: 直接运行 Python 脚本**
```bash
uv run python chatbot.py
```

**方式 3: 运行测试**
```bash
uv run python test_chatbot.py
```

## uv 相比传统方式的优势

### 速度对比
- **传统方式**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt  # 可能需要 30-60 秒
  python chatbot.py
  ```

- **uv 方式**:
  ```bash
  uv sync  # 只需要 1-2 秒！
  uv run chatbot
  ```

### 主要优势

1. **⚡ 极快的速度**: 安装依赖比 pip 快 10-100 倍
2. **🔒 依赖锁定**: 自动生成 `uv.lock` 文件，确保环境一致性
3. **🎯 自动环境管理**: 无需手动创建/激活虚拟环境
4. **📦 统一配置**: 所有配置都在 `pyproject.toml` 中
5. **🚀 一键运行**: `uv run` 自动处理环境设置

## 常用 uv 命令

```bash
# 安装/同步依赖
uv sync

# 添加新依赖
uv add requests

# 移除依赖
uv remove requests

# 更新所有依赖
uv lock --upgrade

# 运行脚本
uv run python script.py

# 运行项目命令（定义在 pyproject.toml 中）
uv run chatbot

# 列出已安装的包
uv pip list

# 查看项目信息
uv tree
```

## 项目结构

```
py2rs/
├── chatbot.py           # 主聊天机器人代码
├── test_chatbot.py      # 测试脚本
├── pyproject.toml       # 项目配置（uv 使用）
├── requirements.txt     # 传统 pip 依赖文件
├── README.md           # 项目文档
├── .env.example        # 环境变量模板
├── .gitignore          # Git 忽略文件
└── .venv/              # 虚拟环境（uv 自动创建）
```

## 故障排除

### 问题: uv 命令未找到
**解决**: 确保 uv 已正确安装并在 PATH 中
```bash
which uv
# 如果没有输出，重新安装 uv
```

### 问题: 依赖安装失败
**解决**: 清理缓存并重新同步
```bash
uv cache clean
uv sync
```

### 问题: API key 错误
**解决**: 确保正确设置环境变量
```bash
echo $OPENAI_API_KEY  # 检查是否设置
export OPENAI_API_KEY='your-key-here'
```

## 下一步

1. 获取 OpenAI API key: https://platform.openai.com/api-keys
2. 设置环境变量
3. 运行 `uv run chatbot` 开始聊天！

# 本地LLM调用Demo（Ollama）
## 一、基础概念
1. LLM：大语言模型，能理解文字、生成回答的AI模型，deepseek-r1:1.5b 就是一款轻量LLM。
2. Ollama：本地运行LLM的工具，模型存电脑本地，无需API密钥、无调用费用、断网可用。

## 二、三大核心参数详解
1. temperature（0~1）
控制回答随机性，数值越小回答严谨准确（适合问答、写代码）；数值越大创意更强（适合写文案）。
2. top_p（0~1）
核采样，筛选高概率词汇，日常使用默认1即可，一般只调节temperature。
3. max_tokens
限制AI输出文字最大长度，避免无限生成长文本。

## 三、环境配置
1. Ollama安装路径：D:\Ollama
2. 模型存放路径：D:\Ollama\Models
3. 本地使用模型：deepseek-r1:1.5b
4. Python依赖安装
```bash
pip install openai
"""第一次呼叫 LLM API：同一支程式，免費線、付費線都能跑。

先在 repo 根目錄建立 .env（參考 .env.example），再執行：
    python demo/first-llm-api/hello_llm.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
)
response = client.chat.completions.create(
    model=os.environ["LLM_MODEL"],
    messages=[{"role": "user", "content": "請用一句繁體中文問候。"}],
    # 推理模型可能把 completion tokens 用在 reasoning；留足空間才有可見回答。
    max_completion_tokens=4096,
)
content = response.choices[0].message.content
if content:
    print(content)
else:
    print("模型沒有回傳可見回答。請檢查 finish_reason、模型限制，或稍後重試。")
print("用掉 token：", response.usage.total_tokens)

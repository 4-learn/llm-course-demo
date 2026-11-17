"""選做：用 embedding API 把句子變成向量（免費線、付費線同一支程式）。

先在 repo 根目錄建立 .env（參考 .env.example），再執行：
    python demo/rag-retrieval/embedding_api.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
)

# NVIDIA 的 embedding 模型要求 input_type（passage＝文件、query＝問題）；OpenAI 不需要。
extra = {"input_type": os.environ["EMBED_INPUT_TYPE"]} if os.environ.get("EMBED_INPUT_TYPE") else {}

response = client.embeddings.create(
    model=os.environ["EMBED_MODEL"],
    input=["退貨需要在收到商品七天內申請。"],
    extra_body=extra,
)
vector = response.data[0].embedding
print("向量長度：", len(vector))
print("前 3 個數字：", [round(x, 4) for x in vector[:3]])

# 從零開始打造 LLM 應用：範例程式

講義：[HackMD 課綱](https://hackmd.io/@yillkid/Hk8hQlgTzl)。每一篇講義開頭的「範例程式碼」會寫出對應的檔案路徑。

## 兩條線，一份程式

呼叫 LLM 的範例都從 `.env` 讀設定。手上是哪一種 key，就填哪一條線；**程式碼完全一樣**。

| | 免費線 | 付費線 |
| --- | --- | --- |
| 模型來源 | [NVIDIA Build](https://build.nvidia.com)（註冊即可拿免費 key） | OpenAI（或課程指定的付費服務） |
| 設定 | `.env.example` 上半段 | `.env.example` 下半段 |
| 注意 | 只限原型、研究、測試；會記錄使用內容，不要送個資 | 會產生費用，先在後台設定用量上限 |

```bash
cp .env.example .env      # Windows：copy .env.example .env
# 打開 .env，填入自己的 key，另一線整段註解掉
```

`.env` 已列在 `.gitignore`，**不要 commit**。

## 內容

| 路徑 | 說明 |
| --- | --- |
| `demo/<主題>/demo.py` | 講義的範例，一個主題一個資料夾。大部分只用標準函式庫，不需網路 |
| `demo/first-llm-api/hello_llm.py` | 第一次呼叫 LLM API（需要 `.env`） |
| `demo/rag-retrieval/embedding_api.py` | 用 embedding API 取得向量（需要 `.env`） |
| `.env.example` | 免費線、付費線設定範本 |

資料夾用主題命名、不加編號，課程插入新章節時不必改名。

## 環境

Python 3.11 以上。

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows：.venv\Scripts\activate
pip install -r requirements.txt
```

所有指令都在 **repo 根目錄**執行，例如：

```bash
python demo/next-word-frequency/demo.py
python demo/first-llm-api/hello_llm.py
```

## 實測紀錄

2026-11-17，Linux、Python 3.12、`openai==3.52.0`：

- 33 支範例全部執行成功（不需網路的範例離線執行）。
- `hello_llm.py`、`embedding_api.py` 兩條線都實際呼叫過：免費線 `nvidia/nemotron-3.5-lightning-30b-a3b`、`nvidia/nemotron-3.5-embed-1b`；付費線 `gpt-5.4-mini`、`text-embedding-3-small`。

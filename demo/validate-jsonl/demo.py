"""逐行驗證 JSONL 結構"""

import json
from io import StringIO

jsonl = '''{"messages":[{"role":"user","content":"請分類：故障"},{"role":"assistant","content":"故障回報"}]}
{"messages":[{"role":"user","content":"請分類：營業時間"},{"role":"assistant","content":"一般詢問"}]}'''

for line_no, line in enumerate(StringIO(jsonl), start=1):
    row = json.loads(line)
    valid = isinstance(row.get("messages"), list) and all(
        isinstance(m, dict) and m.get("role") in {"user", "assistant"}
        and isinstance(m.get("content"), str)
        for m in row["messages"]
    )
    print(f"第 {line_no} 行：{'OK' if valid else '格式錯誤'}")

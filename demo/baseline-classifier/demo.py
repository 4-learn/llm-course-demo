"""建立基準分類器。"""

cases = [
    ("明天下午有社團講座", "活動"),
    ("記得買牛奶", "其他"),
    ("地點還沒公布", "unknown"),
]

for text, expected in cases:
    if "講座" in text or "活動" in text:
        actual = "活動"
    elif "地點" in text:
        actual = "unknown"
    else:
        actual = "其他"
    print(f"輸入：{text}｜預期：{expected}｜分類：{actual}")

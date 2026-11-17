"""把來源與摘要分開"""

results = [
    {"title": "市府公告", "snippet": "活動將於週六上午十點開始。", "url": "https://example.org/event"},
    {"title": "社群貼文", "snippet": "有人說活動改到下午。", "url": "https://example.org/post"},
]

for item in results:
    print(f"來源：{item['title']} ({item['url']})")
    print(f"摘錄：{item['snippet']}")

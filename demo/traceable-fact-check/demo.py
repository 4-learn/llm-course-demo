"""建立可追溯的查核紀錄"""

claims = [
    {"claim": "活動日期為週五", "source": "https://example.org/event", "checked": True},
    {"claim": "免費提供午餐", "source": "", "checked": False},
]

for item in claims:
    traceable = bool(item["source"].startswith("https://")) and item["checked"]
    status = "待人工查核" if traceable else "缺來源或未核對"
    print(f"{item['claim']}：{status}")

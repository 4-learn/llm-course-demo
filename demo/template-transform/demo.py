"""檢查資料再格式化"""

record = {"name": "林同學", "status": "待確認", "amount": 180}

def render_summary(item):
    if not isinstance(item.get("name"), str):
        raise ValueError("name 必須是文字")
    if not isinstance(item.get("amount"), int):
        raise ValueError("amount 必須是整數")
    return f"{item['name']}：{item['status']}，金額 {item['amount']} 元"

print(render_summary(record))

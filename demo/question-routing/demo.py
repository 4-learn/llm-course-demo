"""簡單分流基線"""

def route(question):
    if "退貨" in question or "退款" in question:
        return "退貨知識庫"
    if "訂單" in question or "配送" in question:
        return "訂單知識庫"
    return "人工確認"

for q in ["怎麼申請退款？", "訂單配送到哪了？", "你們週末有開嗎？"]:
    print(f"{q} -> {route(q)}")

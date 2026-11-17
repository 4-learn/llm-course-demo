"""用 Python 描述一條流程"""

def classify(question):
    if "退貨" in question:
        return "退貨說明"
    if "訂單" in question:
        return "訂單查詢"
    return "人工確認"

for question in ["退貨要幾天？", "我的訂單到哪了？", "嗨"]:
    print(f"{question} -> {classify(question)}")

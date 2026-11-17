"""用 Python 模擬對話路由"""

def reply(message):
    text = message.strip()
    if not text:
        return "請輸入想查詢的活動。"
    if "活動" in text:
        return "已收到活動查詢；請提供名稱或日期以便查證。"
    return "目前只處理活動查詢，請補充活動關鍵字。"

for message in ("", "想查活動", "你好"):
    print(reply(message))

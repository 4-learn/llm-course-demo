"""拆分處理步驟"""

def normalize(text):
    return " ".join(text.strip().split())

def route(text):
    clean = normalize(text)
    if not clean:
        return "請輸入問題"
    if "退貨" in clean:
        return "退貨流程"
    return "一般問答流程"

for message in ["  想辦理退貨  ", "你好", "   "]:
    print(f"{message!r} -> {route(message)}")

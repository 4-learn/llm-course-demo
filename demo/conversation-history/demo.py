"""建立最小對話紀錄"""

messages = []
messages.append({"role": "user", "content": "我喜歡茶。"})
messages.append({"role": "assistant", "content": "你喜歡茶。"})
messages.append({"role": "user", "content": "我剛才說喜歡什麼？"})
print("訊息筆數：", len(messages))
print("最後一則：", messages[-1]["content"])

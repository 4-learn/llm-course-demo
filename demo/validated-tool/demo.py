"""安全執行一個工具"""

def count_letter(text, letter):
    if not isinstance(text, str) or not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("需要文字和單一字元")
    return text.count(letter)

request = {"name": "count_letter", "arguments": {"text": "banana", "letter": "a"}}
allowed_tools = {"count_letter": count_letter}
if request["name"] not in allowed_tools:
    raise ValueError("未知工具")
result = allowed_tools[request["name"]](**request["arguments"])
print("工具結果：", result)

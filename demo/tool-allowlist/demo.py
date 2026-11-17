"""工具白名單"""

ALLOWED = {"search_public_docs", "summarize_text"}

def authorize(tool_name, args):
    if tool_name not in ALLOWED:
        return False
    if not isinstance(args, dict):
        return False
    return True

print(authorize("summarize_text", {"text": "公開說明"}))
print(authorize("send_email", {"to": "someone@example.com"}))

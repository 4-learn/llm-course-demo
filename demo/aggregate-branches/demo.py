"""合併分支結果"""

def aggregate(route_a=None, route_b=None):
    candidates = [x for x in (route_a, route_b) if isinstance(x, str) and x.strip()]
    if not candidates:
        return {"status": "no_result", "answer": None}
    return {"status": "ok", "answer": candidates[0]}

print(aggregate(route_a="由分支 A 找到的摘要"))
print(aggregate())

"""定義一個安全的純函式工具"""

def lookup_order(order_id, orders):
    if not isinstance(order_id, str) or not order_id.startswith("ORD-"):
        return {"ok": False, "error": "invalid_order_id"}
    if order_id not in orders:
        return {"ok": False, "error": "not_found"}
    return {"ok": True, "status": orders[order_id]}

orders = {"ORD-1001": "配送中"}
print(lookup_order("ORD-1001", orders))
print(lookup_order("bad", orders))
print(lookup_order("ORD-9999", orders))

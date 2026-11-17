"""本地關鍵字檢索"""

docs = ["蘋果是水果。", "茶可以熱飲或冷飲。", "香蕉通常是黃色。"]
query = "蘋果"
hits = [doc for doc in docs if query in doc]
print("候選資料：", hits)

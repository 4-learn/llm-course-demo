"""本地檢索與帶來源的回覆草稿"""

docs = [
    {"source": "A", "text": "課程每週三下午上課。"},
    {"source": "B", "text": "作業請在週五前繳交。"},
]
query = "哪天上課"
hits = [d for d in docs if "上課" in d["text"]]
if hits:
    print("候選答案：", hits[0]["text"])
    print("來源：", hits[0]["source"])
else:
    print("資料不足，請查證。")

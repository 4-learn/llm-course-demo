"""保留文件來源"""

documents = [
    {"id": "KB-01", "source": "退貨政策", "text": "商品到貨七日內可申請退貨。"},
    {"id": "KB-02", "source": "配送說明", "text": "訂單成立後可至會員頁查詢配送狀態。"},
]
query = "退貨"
hits = [doc for doc in documents if query in doc["text"]]
for doc in hits:
    print(f"{doc['id']}｜{doc['source']}｜{doc['text']}")

"""檢查微調資料"""

examples = [
    {"instruction": "退貨期限？", "input": "", "output": "請於收貨後七日內申請。"},
    {"instruction": "訂單怎麼查？", "input": "", "output": "到會員頁查看訂單狀態。"},
]

required = {"instruction", "input", "output"}
for i, row in enumerate(examples, start=1):
    assert set(row) == required and all(isinstance(row[k], str) for k in required)
    assert row["instruction"].strip() and row["output"].strip()
    print(f"example {i}: valid")
print(f"total: {len(examples)}")

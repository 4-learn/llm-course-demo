"""程式檢查驗收清單"""

checks = {
    "需求與範圍": True,
    "固定測試案例": True,
    "輸出與權限驗證": False,
    "資料保存與刪除規則": False,
}
missing = [name for name, done in checks.items() if not done]
print("可進入試用" if not missing else "尚未就緒：" + "、".join(missing))

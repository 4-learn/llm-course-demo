"""拆解問題並迭代"""

question = "想知道台北到高雄的交通方式，以及高雄有哪些夜市？"
subquestions = [
    "台北到高雄有哪些交通方式？",
    "高雄有哪些夜市？",
]

if not subquestions:
    print("請補充想查詢的問題。")
else:
    for i, item in enumerate(subquestions, start=1):
        print(f"子問題 {i}: {item}")

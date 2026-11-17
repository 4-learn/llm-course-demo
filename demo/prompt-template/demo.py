"""建立可重用的提示模板"""

template = "任務：{task}\n輸入：{text}\n要求：只列出候選分類；不確定請寫 unknown。"
print(template.format(task="分類活動訊息", text="地點尚未公布"))

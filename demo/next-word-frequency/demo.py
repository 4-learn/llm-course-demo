"""用詞頻預測下一個詞"""

sentences = ["我 喜歡 蘋果", "我 喜歡 香蕉", "我 喜歡 蘋果"]
counts = {}
for sentence in sentences:
    words = sentence.split()
    pair = (words[0], words[1])
    counts.setdefault(pair, {})
    counts[pair][words[2]] = counts[pair].get(words[2], 0) + 1

next_word = max(counts[("我", "喜歡")], key=counts[("我", "喜歡")].get)
print("前文：我 喜歡")
print("最常見的下一詞：" + next_word)

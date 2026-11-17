"""精確比對"""

cases = [
    ("strawberry", "r", 3),
    ("banana", "a", 3),
    ("apple", "p", 2),
    ("kiwi", "z", 0),
]
predictions = [text.count(char) for text, char, _ in cases]
correct = sum(pred == expected for pred, (_, _, expected) in zip(predictions, cases))
for (text, char, expected), pred in zip(cases, predictions):
    print(f"{text!r} 中 {char!r}: expected={expected}, actual={pred}")
print(f"accuracy: {correct}/{len(cases)} = {correct / len(cases):.2f}")

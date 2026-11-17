"""加權混合向量"""

a = [1.0, 0.0]
b = [0.0, 1.0]
w_a, w_b = 0.7, 0.3
mixed = [w_a * x + w_b * y for x, y in zip(a, b)]
print(mixed)

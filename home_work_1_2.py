# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

W = not None
Z = not None
Y = not None
X = not None
W != X
W != Y
W != Z
X != Y
X != Z
Y != Z

print((W and Z) or (not Y) or (not X is not W))
# В условии перепутаны знаки "⋀" и "⋁"
print((W or Z) and (not Y) and (not X is not W))

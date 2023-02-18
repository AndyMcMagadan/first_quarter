# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

mount_of_choice = range(2)
print("w", "x", "y", "z")

for w in mount_of_choice:
    for x in mount_of_choice:
        for y in mount_of_choice:
            for z in mount_of_choice:
                if not ((w and z) or (not y) or (not x is not w)):
                    print(w, x, y, z)

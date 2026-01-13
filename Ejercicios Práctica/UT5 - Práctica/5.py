import random

original: list[int] = []

for _ in range(10):
    original.append(random.randint(1, 100))

ordenada: list[int] = sorted(original)

print(f"Lista original: {original}")
print(f"Lista ordenada: {ordenada}")
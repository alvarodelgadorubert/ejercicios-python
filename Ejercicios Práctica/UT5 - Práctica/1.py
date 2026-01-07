nombres = ["Ana", "Benja", "Carlos", "Dario"]
print(f"Lista inicial: {nombres}")

nombres.append("Elena")
nombres.insert(1, "Fernando")
nombres.pop(2)

print(f"La lista tiene {len(nombres)} elementos.")
print(f"Lista final: {nombres}")
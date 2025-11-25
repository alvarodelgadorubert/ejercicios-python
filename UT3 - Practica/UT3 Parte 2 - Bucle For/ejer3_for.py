n = int(input("¿Cuántos números vas a introducir? "))
may = men = eq = 0
for _ in range(n):
    num = float(input("Introduce un número: "))
    if num > 0: may += 1
    elif num < 0: men += 1
    else: eq += 1
print(may, men, eq)
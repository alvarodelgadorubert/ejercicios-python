total = 0.0

for mes in range(1, 13):
    cantidad = float(input(f"Introduce cuánto has ahorrado en el mes {mes}: "))
    total += cantidad
    print(f"Llevas ahorrado: {total:.2f} €")

print(f"Ahorro total del año: {total:.2f} €")
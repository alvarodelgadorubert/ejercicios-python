pago = 10
total = 0

for mes in range(1, 11):
    print(f"Mes {mes}: {pago} €")
    total += pago
    pago *= 2

print(f"Total pagado tras 10 meses: {total} €")
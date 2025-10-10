monedas_2e = int(input("Número de monedas de 2€: "))
monedas_1e = int(input("Número de monedas de 1€: "))
monedas_50c = int(input("Número de monedas de 50 céntimos: "))
monedas_20c = int(input("Número de monedas de 20 céntimos: "))
monedas_10c = int(input("Número de monedas de 10 céntimos: "))

total_euros = (monedas_2e * 2) + (monedas_1e * 1) + (monedas_50c * 0.5) + (monedas_20c * 0.2) + (monedas_10c * 0.1)
euros_enteros = int(total_euros)
centimos = round((total_euros - euros_enteros) * 100)

print(f"Total: {euros_enteros} euros y {centimos} céntimos")
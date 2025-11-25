n = int(input("¿Cuántos trabajadores tiene la empresa?: "))
precio_hora = float(input("¿Cuánto se paga por hora?: "))

total_empresa = 0.0

for i in range(1, n + 1):
    horas = float(input(f"Horas trabajadas por el trabajador {i}: "))
    sueldo = horas * precio_hora
    print(f"Sueldo del trabajador {i}: {sueldo:.2f} €")
    total_empresa += sueldo

print(f"La empresa pagará un total de: {total_empresa:.2f} €")
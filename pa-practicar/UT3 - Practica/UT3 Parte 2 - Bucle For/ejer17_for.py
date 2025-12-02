n = int(input("¿Cuántos trabajadores tiene la empresa?: "))
precio_hora = float(input("¿Cuánto se paga por hora?: "))

total_empresa = 0.0

for t in range(1, n + 1):
    print(f"\nTrabajador {t}")
    dias = int(input("¿Cuántos días ha trabajado?: "))
    
    horas_trabajador = 0.0
    for d in range(1, dias + 1):
        h = float(input(f"Horas trabajadas en el día {d}: "))
        horas_trabajador += h
    
    sueldo = horas_trabajador * precio_hora
    print(f"Sueldo del trabajador {t}: {sueldo:.2f} €")
    total_empresa += sueldo

print(f"\nTotal que pagará la empresa: {total_empresa:.2f} €")
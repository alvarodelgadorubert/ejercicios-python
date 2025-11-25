total_horas = 0.0
precio_hora = float(input("¿Cuánto cobra por hora?: "))

for dia in range(1, 7):
    horas = float(input(f"Horas trabajadas el día {dia}: "))
    total_horas += horas

sueldo = total_horas * precio_hora

print(f"Horas totales trabajadas: {total_horas}")
print(f"Sueldo semanal: {sueldo:.2f} €")
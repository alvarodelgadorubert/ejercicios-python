dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
minimas = []
maximas = []

for dia in dias:
    min_temp = float(input(f"Mínima del {dia}: "))
    max_temp = float(input(f"Máxima del {dia}: "))
    minimas.append(min_temp)
    maximas.append(max_temp)

print("\nMedia de cada día:")
for i in range(7):
    media = (minimas[i] + maximas[i]) / 2
    print(f"{dias[i]}: {media:.2f}")

temp_min_absoluta = min(minimas)
print(f"\nDías con menos temperatura ({temp_min_absoluta}):")
for i in range(7):
    if minimas[i] == temp_min_absoluta:
        print(dias[i])

buscar_max = float(input("\nIntroduce una temperatura máxima para buscar: "))
encontrado = False
for i in range(7):
    if maximas[i] == buscar_max:
        print(f"El {dias[i]} coincide con esa temperatura máxima.")
        encontrado = True

if not encontrado:
    print("No hay ningún día que coincida con esa temperatura máxima.")
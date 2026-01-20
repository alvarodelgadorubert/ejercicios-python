nombres = []
edades = []

while True:
    nombre = input("Introduce el nombre del alumno (o * para terminar): ")
    if nombre == "*":
        break
    edad = int(input(f"Introduce la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)

print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"{nombres[i]} - {edades[i]} años")

if edades:
    edad_maxima = max(edades)
    print("\nAlumnos con la edad máxima:")
    for i in range(len(nombres)):
        if edades[i] == edad_maxima:
            print(f"{nombres[i]} - {edades[i]} años")
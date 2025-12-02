from pathlib import Path

nombre_aula = input("Introduce el nombre del aula: ")

while True:
    try:
        M = int(input("Introduce el número de equipos (M): "))
        if M > 0:
            break
        else:
            print("El número de equipos debe ser positivo.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

ruta_aula = Path.cwd() / nombre_aula

if not ruta_aula.exists():
    ruta_aula.mkdir()
    print(f"\nCarpeta del aula '{nombre_aula}' creada.")
else:
    print(f"\nCarpeta del aula '{nombre_aula}' ya existe.")

for i in range(1, M + 1):
    numero_pc = str(i).zfill(2)
    nombre_pc = f"PC-{numero_pc}"
    ruta_pc = ruta_aula / nombre_pc
    
    if ruta_pc.exists():
        print(f"  -> La carpeta '{nombre_pc}' ya existía en '{nombre_aula}'.")
    else:
        ruta_pc.mkdir()
        print(f"  -> Carpeta '{nombre_pc}' creada en '{nombre_aula}'.")
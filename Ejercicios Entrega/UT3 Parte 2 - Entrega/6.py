from pathlib import Path

while True:
    try:
        N = int(input("Introduce el número de carpetas a crear (N): "))
        if N > 0:
            break
        else:
            print("Introduce un número positivo.")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

directorio_actual = Path.cwd()

for i in range(1, N + 1):
    nombre_carpeta = f"backup_{i}"
    ruta_carpeta = directorio_actual / nombre_carpeta
    
    if ruta_carpeta.exists():
        print(f"La carpeta '{nombre_carpeta}' ya existía.")
    else:
        ruta_carpeta.mkdir()
        print(f"La carpeta '{nombre_carpeta}' ha sido creada.")
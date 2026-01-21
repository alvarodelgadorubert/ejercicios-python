from pathlib import Path

rutas_pedidas: list[str] = []
for i in range(4):
    rutas_pedidas.append(input(f"Introduce ruta {i+1}: "))

analisis: dict[str, str] = {}
for r in rutas_pedidas:
    p = Path(r)
    if not p.exists():
        analisis[r] = "no existe"
    elif p.is_file():
        analisis[r] = "fichero"
    elif p.is_dir():
        analisis[r] = "directorio"

for ruta, tipo in analisis.items():
    print(f"{ruta}: {tipo}")
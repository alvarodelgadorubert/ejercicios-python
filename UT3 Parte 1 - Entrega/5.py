from pathlib import Path
import os

ruta_actual = Path.cwd()
print(ruta_actual)

contenido = os.listdir(ruta_actual)
print(contenido)

carpeta_logs = ruta_actual / "logs"

if not carpeta_logs.exists():
    carpeta_logs.mkdir()
    print("Carpeta creada")
else:
    print("Carpeta ya existe")
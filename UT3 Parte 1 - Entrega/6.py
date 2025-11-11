import shutil
from pathlib import Path

archivo_config = Path("config.ini")
archivo_ejemplo = Path("config.example.ini")

if archivo_config.exists():
    print("Config existente")
else:
    if archivo_ejemplo.exists():
        shutil.copy(archivo_ejemplo, archivo_config)
    else:
        print("Falta el archivo de ejemplo")
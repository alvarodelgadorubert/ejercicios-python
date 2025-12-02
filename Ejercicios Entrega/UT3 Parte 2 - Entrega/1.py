# Ejercicio 1
from pathlib import Path

contador_logs = 0
directorio_actual = Path.cwd()

for elemento in directorio_actual.iterdir():
    if elemento.is_file() and str(elemento).endswith(".log"):
        contador_logs += 1

print(f"Total de archivos .log encontrados: {contador_logs}")
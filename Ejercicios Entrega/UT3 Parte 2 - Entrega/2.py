# Ejercicio 2
from pathlib import Path

tamano_total_bytes = 0
UN_MEGABYTE = 1048576
directorio_actual = Path.cwd()

for elemento in directorio_actual.iterdir():
    if elemento.is_file() and str(elemento).endswith(".log"):
        tamano_total_bytes += elemento.stat().st_size

print(f"Tamaño total de logs: {tamano_total_bytes} bytes")

if tamano_total_bytes >= UN_MEGABYTE:
    print("ALTO VOLUMEN")
else:
    print("OK")
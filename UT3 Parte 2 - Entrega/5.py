# Ejercicio 5
from pathlib import Path
from datetime import datetime

directorio_actual = Path.cwd()

print("--- Archivos .log y Fecha de Modificación ---")

for elemento in directorio_actual.iterdir():
    if elemento.is_file() and str(elemento).endswith(".log"):
        nombre_archivo = elemento.name
        
        tiempo_modificacion_timestamp = elemento.stat().st_mtime
        
        fecha_modificacion = datetime.fromtimestamp(tiempo_modificacion_timestamp)
        
        print(f"Archivo: {nombre_archivo} | Modificado: {fecha_modificacion}")
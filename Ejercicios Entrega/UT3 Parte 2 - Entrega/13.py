from pathlib import Path
from datetime import datetime

archivo_mas_reciente = None
tiempo_modificacion_max = 0
directorio_actual = Path.cwd()
archivos_encontrados = False

for elemento in directorio_actual.iterdir():
    if elemento.is_file():
        archivos_encontrados = True
        tiempo_modificacion_actual = elemento.stat().st_mtime
        
        if tiempo_modificacion_actual > tiempo_modificacion_max:
            tiempo_modificacion_max = tiempo_modificacion_actual
            archivo_mas_reciente = elemento

if archivo_mas_reciente:
    fecha_modificacion = datetime.fromtimestamp(tiempo_modificacion_max)
    
    print("--- Archivo con Fecha de Modificación Más Reciente ---")
    print(f"Archivo: {archivo_mas_reciente.name}")
    print(f"Fecha/Hora de Modificación: {fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print("Sin archivos en el directorio actual.")
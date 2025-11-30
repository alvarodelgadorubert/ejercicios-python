from pathlib import Path

while True:
    nombre_archivo = input("Introduce un nombre de archivo: ")
    ruta_archivo = Path(nombre_archivo)
    
    if ruta_archivo.is_file():
        tamano_bytes = ruta_archivo.stat().st_size
        print(f"Archivo '{nombre_archivo}' encontrado.")
        print(f"Tamaño: {tamano_bytes} bytes")
        break
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Inténtalo de nuevo.")
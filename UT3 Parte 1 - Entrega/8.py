import sys
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit()

nombre_archivo = sys.argv[1]
ruta_archivo = Path(nombre_archivo)

UN_MB = 1_048_576

if not ruta_archivo.exists() or not ruta_archivo.is_file():
    sys.exit()

info_archivo = ruta_archivo.stat()
tamano_bytes = info_archivo.st_size

if tamano_bytes >= UN_MB:
    print("GRANDE")
else:
    print("PEQUEÑO")
from pathlib import Path

contenido: dict[str, str] = {}
for p in Path('.').iterdir():
    if p.is_file():
        contenido[p.name] = "fichero"
    else:
        contenido[p.name] = "directorio"

print(contenido)
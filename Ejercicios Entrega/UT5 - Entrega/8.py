import platform
import os
from datetime import datetime
from pathlib import Path

rutas: list[str] = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
informe_rutas: dict[str, str] = {}

for r in rutas:
    p = Path(r)
    if not p.exists():
        informe_rutas[r] = "no existe"
    else:
        informe_rutas[r] = "archivo" if p.is_file() else "directorio"

print(f"Sistema: {platform.system()}")
print(f"CPUs: {os.cpu_count()}")
print(f"Fecha: {datetime.now()}")
print(f"Estado rutas: {informe_rutas}")
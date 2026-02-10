from pathlib import Path

# Preparación
Path("logs").mkdir(exist_ok=True)
for f in ["auth.log", "syslog.log", "script.py", "data.txt"]:
    (Path("logs") / f).touch()

for archivo in Path("logs").glob("*.log"):
    print(archivo.name)
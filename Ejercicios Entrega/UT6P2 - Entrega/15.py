from pathlib import Path

for archivo in Path("logs").glob("*.log"):
    tamano = archivo.stat().st_size
    print(f"{archivo.name} {tamano}")
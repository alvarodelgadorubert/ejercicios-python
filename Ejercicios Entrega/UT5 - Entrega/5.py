from pathlib import Path

nombres_carpetas: list[str] = ["logs", "data", "backup"]
carpetas_path: list[Path] = [Path(n) for n in nombres_carpetas]

resultado: dict[str, str] = {}
for p in carpetas_path:
    if p.exists():
        resultado[p.name] = "ya existía"
    else:
        p.mkdir()
        resultado[p.name] = "creada"

print(resultado)
from pathlib import Path

home_path = Path('/home')
conteo_archivos: dict[str, int] = {}

if home_path.exists():
    for usuario_dir in home_path.iterdir():
        if usuario_dir.is_dir():
            archivos = [f for f in usuario_dir.iterdir() if f.is_file()]
            conteo_archivos[usuario_dir.name] = len(archivos)

print(conteo_archivos)
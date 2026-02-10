from pathlib import Path

rutas = ["/etc", "/etc/passwd", "no_existe.txt", "."]
with open("paths.txt", "w") as f:
    for r in rutas:
        f.write(r + "\n")

with open("paths.txt", "r") as f_in, open("paths_status.txt", "w") as f_out:
    for linea in f_in:
        ruta_str = linea.strip()
        p = Path(ruta_str)
        
        if not p.exists():
            estado = "No Existe"
        elif p.is_dir():
            estado = "Directorio"
        elif p.is_file():
            estado = "Archivo"
        else:
            estado = "Otro"
            
        f_out.write(f"{ruta_str} -> {estado}\n")
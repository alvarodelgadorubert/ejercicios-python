from pathlib import Path

carpetas = ["/tmp", "/var/tmp", "/usr/bin", "/noexiste"]
with open("cleanup_plan.txt", "w") as f:
    for c in carpetas:
        f.write(c + "\n")

with open("cleanup_plan.txt", "r") as f_in, open("cleanup_report.txt", "w") as f_out:
    for linea in f_in:
        ruta_str = linea.strip()
        p = Path(ruta_str)
        
        if p.exists():
            elementos = len(list(p.iterdir()))
            f_out.write(f"{ruta_str} -> existe -> elementos: {elementos}\n")
        else:
            f_out.write(f"{ruta_str} -> NO existe\n")
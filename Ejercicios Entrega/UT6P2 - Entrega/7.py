from pathlib import Path

with open("users.txt", "r") as f_in, open("homes_check.txt", "w") as f_out:
    for linea in f_in:
        user, path_str = linea.strip().split(", ")
        p = Path(path_str)
        estado = "OK" if p.exists() else "No existe"
        f_out.write(f"{user} -> {path_str} -> {estado}\n")
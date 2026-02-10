from pathlib import Path

usuario = input("Nombre de usuario: ")
home_estimada = Path("/home") / usuario

usuarios_existentes = []
if Path("users.txt").exists():
    with open("users.txt", "r") as f:
        for linea in f:
            usuarios_existentes.append(linea.split(",")[0])

if usuario not in usuarios_existentes:
    with open("users.txt", "a") as f:
        f.write(f"{usuario}, {home_estimada}\n")
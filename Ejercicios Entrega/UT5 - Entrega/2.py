import os

nombres: list[str] = []
for i in range(3):
    nombres.append(input(f"Introduce nombre de usuario {i+1}: "))

homes: dict[str, str] = {}
for nombre in nombres:
    homes[nombre] = os.path.expanduser(f"~{nombre}")

for usuario, ruta in homes.items():
    print(f"Usuario: {usuario} -> Home: {ruta}")
path_original: str = "/usr/local/bin:/usr/bin:/bin"
lista_path: list[str] = path_original.split(":")

nueva_al_final: str = input("Ruta para añadir al final: ")
nueva_al_inicio: str = input("Ruta para añadir al inicio: ")

lista_path.append(nueva_al_final)
lista_path.insert(0, nueva_al_inicio)

for p in lista_path:
    print(p)

resultado_final: str = ":".join(lista_path)
print(f"Resultado: {resultado_final}")
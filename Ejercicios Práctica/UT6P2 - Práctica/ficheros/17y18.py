config = {}
with open("config.txt", "r") as f:
    for linea in f:
        partes = linea.split()
        if len(partes) == 2:
            config[partes[0]] = partes[1]

busqueda = input("¿Qué clave buscas? ")
if busqueda in config:
    print(f"Valor: {config[busqueda]}")
else:
    print("La clave no existe.")
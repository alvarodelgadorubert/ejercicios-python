config_data = "port=8080\nmode=prod\nuser=admin"
with open("service.conf", "w") as f:
    f.write(config_data)

config_dict = {}
with open("service.conf", "r") as f:
    for linea in f:
        clave, valor = linea.strip().split("=")
        config_dict[clave] = valor

busqueda = input("Introduce la clave a buscar: ")
print(config_dict.get(busqueda, "La clave no existe"))
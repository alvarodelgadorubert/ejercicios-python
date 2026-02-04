nombre_fich = input("Introduce el nombre del archivo a leer: ")
try:
    with open(nombre_fich, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_fich}' no existe.")
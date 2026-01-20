datos: dict[str, str] = {}

for _ in range(3):
    clave = input("Introduce la clave: ")
    valor = input("Introduce el valor: ")
    datos[clave] = valor

print(datos)
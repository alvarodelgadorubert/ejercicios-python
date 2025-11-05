import platform

print("Sistema operativo: ",platform.system())
print("Versión: ",platform.release())
print("Procesador: ",platform.processor())

if platform.system() == "Windows":
    print("El gestor de paquetes recomendado es Winget")
elif platform.system() == "Linux":
    print("El gestor de paquetes recomendado es apt")
elif platform.system() == "macOS (Darwin)":
    print("El gestor de paquetes recomendado es brew")
else:
    print("Gestor no definido")
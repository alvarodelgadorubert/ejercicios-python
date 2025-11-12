import platform

so = platform.system()
version = platform.release()
procesador = platform.processor()

print(f"Sistema Operativo: {so}")
print(f"Versión: {version}")
print(f"Procesador: {procesador}")

if so == "Windows":
    gestor_recomendado = "winget"
elif so == "Linux":
    gestor_recomendado = "apt"
elif so == "macOS (Darwin)":
    gestor_recomendado = "brew"
else:
    gestor_recomendado = "gestor no definido"

print(gestor_recomendado)
paquetes: list[str] = ["vim", "curl", "htop"]
nuevo: str = input("Añade un paquete más: ")
paquetes.append(nuevo)

comando: str = "apt install " + " ".join(paquetes)
print(comando)
# 1. Pedir el nombre de usuario
usuario = input("Nombre de usuario: ")

# 2. Pedir la contraseña
contrasena = input("Contraseña: ")

# 3. Comprobar si ambos coinciden con "pepe" Y "asdasd"
if usuario == "pepe" and contrasena == "asdasd":
    print("¡Has entrado al sistema!")
else:
    print("Error: Usuario o contraseña incorrectos.")
from datetime import datetime

mensaje = input("Introduce el mensaje para el log: ")
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("admin_log.txt", "a") as f:
    f.write(f"[{fecha_hora}] {mensaje}\n")
ficheros = ["saludo.txt", "numeros.txt", "config.txt"]
with open("daily_backup_list.txt", "w") as f:
    for fic in ficheros:
        f.write(fic + "\n")

destino = "/backup"
with open("daily_backup_list.txt", "r") as f_in, open("backup_commands.txt", "w") as f_out:
    for linea in f_in:
        origen = linea.strip()
        f_out.write(f"cp {origen} {destino}/{origen}\n")
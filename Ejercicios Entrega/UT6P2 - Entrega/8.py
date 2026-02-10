comandos = ["ls -la", "df -h", "uname -a", "top"]
with open("commands.txt", "w") as f:
    for c in comandos:
        f.write(c + "\n")

with open("commands.txt", "r") as f_in, open("commands_numbered.txt", "w") as f_out:
    for i, linea in enumerate(f_in, 1):
        f_out.write(f"{i}: {linea}")
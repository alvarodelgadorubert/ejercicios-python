usuarios = {}
with open("datos.csv", "r") as f:
    for linea in f:
        n, e = linea.strip().split(",")
        usuarios[n] = int(e)
print(usuarios)
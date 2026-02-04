try:
    with open("contador.txt", "r") as f:
        valor = int(f.read().strip())
except FileNotFoundError:
    valor = 0

valor += 1

with open("contador.txt", "w") as f:
    f.write(str(valor))
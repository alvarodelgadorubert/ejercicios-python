with open("nombres.txt", "w") as f:
    for i in range(5):
        nombre = input(f"Introduce el nombre {i+1}: ")
        f.write(nombre + "\n")
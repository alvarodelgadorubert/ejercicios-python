with open("datos.csv", "w") as f:
    f.write("Pepe,25\nAna,30\nLuis,22\n")

with open("datos.csv", "r") as f:
    for linea in f:
        nombre, edad = linea.strip().split(",")
        print(f"Nombre: {nombre}, Edad: {edad}")
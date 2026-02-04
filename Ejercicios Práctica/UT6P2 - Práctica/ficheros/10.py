palabra = input("Dime una palabra para añadir: ")
with open("palabras.txt", "a") as f:
    f.write(palabra + "\n")
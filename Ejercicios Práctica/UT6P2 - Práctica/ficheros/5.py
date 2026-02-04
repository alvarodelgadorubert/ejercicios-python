with open("numeros.txt", "r") as f:
    for linea in f:
        num = int(linea.strip())
        if num % 2 == 0:
            print(num)
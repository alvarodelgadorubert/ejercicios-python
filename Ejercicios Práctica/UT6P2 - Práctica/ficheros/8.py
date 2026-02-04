with open("nombres.txt", "r") as f:
    nombres = [n.strip() for n in f.readlines()]
    print(f"El más largo es: {max(nombres, key=len)}")
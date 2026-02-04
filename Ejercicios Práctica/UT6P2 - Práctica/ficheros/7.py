with open("nombres.txt", "r") as f:
    total = len(f.readlines())
    print(f"Hay {total} nombres.")
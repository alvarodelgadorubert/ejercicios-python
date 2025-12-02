for n in range(1, 6):
    print(f"\nTabla del {n}")
    for i in range(1, 11):
        resultado = n * i
        if resultado % 3 == 0:
            continue
        print(f"{n} x {i} = {resultado}")
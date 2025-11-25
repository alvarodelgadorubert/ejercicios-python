for _ in range(1000000):
    c = input("Introduce un carácter (espacio para terminar): ")
    if len(c)!=1:
        print("Introduce un único carácter.")
        continue
    if c==" ":
        break
    print("VOCAL" if c.lower() in "aeiou" else "NO VOCAL")
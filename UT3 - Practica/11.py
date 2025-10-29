try:
    # 1. Pedir los tres lados
    a = float(input("Introduce la longitud del lado A: "))
    b = float(input("Introduce la longitud del lado B: "))
    c = float(input("Introduce la longitud del lado C: "))

    # 2. Comprobar si es un triángulo válido
    # La suma de dos lados siempre debe ser mayor que el tercero
    if (a + b <= c) or (a + c <= b) or (b + c <= a) or a<=0 or b<=0 or c<=0:
        print("Esos lados NO pueden formar un triángulo.")
    
    else:
        # 3. Si es válido, clasificar (Equilátero, Isósceles, Escaleno)
        # Empezamos por el más específico (Equilátero)
        
        print("El triángulo es VÁLIDO.")
        
        if a == b and b == c:
            print("Es un triángulo EQUILÁTERO.")
        elif a == b or b == c or a == c:
            print("Es un triángulo ISÓSCELES.")
        else:
            print("Es un triángulo ESCALENO.")

        # 4. Comprobar por separado si es Rectángulo (Pitágoras)
        # Hay que encontrar la hipotenusa (el lado más largo)
        
        h = 0.0 # Hipotenusa
        c1 = 0.0 # Cateto 1
        c2 = 0.0 # Cateto 2

        if a >= b and a >= c:
            h = a
            c1 = b
            c2 = c
        elif b >= a and b >= c:
            h = b
            c1 = a
            c2 = c
        else:
            h = c
            c1 = a
            c2 = b
        
        # Comprobar Pitágoras (h^2 = c1^2 + c2^2)
        # Usamos tolerancia (abs) por ser números 'float'
        if abs(h**2 - (c1**2 + c2**2)) < 0.00001:
            print("Además, es un triángulo RECTÁNGULO.")

except ValueError:
    print("Error: Los lados deben ser números.")
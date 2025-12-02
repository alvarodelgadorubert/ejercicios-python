while True:
    password = input("Introduce una contraseña: ")
    
    if len(password) < 6:
        print("Error: La contraseña debe tener al menos 6 caracteres.")
        continue

    tiene_digito = False
    
    for caracter in password:
        if caracter.isdigit():
            tiene_digito = True
            break
            
    if not tiene_digito:
        print("Error: La contraseña debe contener al menos un dígito.")
        continue
        
    print("Contraseña validada correctamente.")
    break
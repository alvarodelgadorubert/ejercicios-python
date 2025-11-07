while True:
    caracter = input()

    if caracter == ' ':
        break 

    if len(caracter) != 1:
        continue

    caracter_lower = caracter.lower()

    if caracter_lower == 'a' or caracter_lower == 'e' or caracter_lower == 'i' or caracter_lower == 'o' or caracter_lower == 'u':
        print("VOCAL")
    else:
        print("NO VOCAL")
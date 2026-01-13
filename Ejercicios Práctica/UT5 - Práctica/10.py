lista_compra: list[str] = []

while True:
    print("\nGestión de Lista de la Compra")
    print("1. Mostrar la lista")
    print("2. Añadir elementos a la lista")
    print("3. Borrar elementos de la lista")
    print("4. Contar elementos de la lista")
    print("5. Añadir una lista de elementos a la ya existente")
    print("6. Borrar toda la lista")
    print("7. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Lista: {lista_compra}")
    elif opcion == "2":
        item = input("Elemento a añadir: ")
        lista_compra.append(item)
    elif opcion == "3":
        item = input("Elemento a borrar: ")
        if item in lista_compra:
            lista_compra.remove(item)
        else:
            print("No está en la lista.")
    elif opcion == "4":
        print(f"Total de elementos: {len(lista_compra)}")
    elif opcion == "5":
        items_str = input("Introduce elementos separados por coma: ")
        nuevos_items = items_str.split(",")
        lista_compra.extend(nuevos_items)
    elif opcion == "6":
        lista_compra.clear()
        print("Lista borrada.")
    elif opcion == "7":
        break
    else:
        print("Opción no válida.")
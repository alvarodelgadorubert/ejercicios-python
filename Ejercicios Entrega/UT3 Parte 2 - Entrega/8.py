from pathlib import Path

directorio_actual = Path.cwd()

while True:
    print("\n--- Menú de Administración ---")
    print("1) Listar archivos del directorio actual")
    print("2) Crear carpeta 'logs'")
    print("3) Salir")
    
    opcion = input("Selecciona una opción (1, 2, o 3): ")
    
    if opcion == '1':
        print("\nContenido del directorio actual:")
        for elemento in directorio_actual.iterdir():
            print(f"- {elemento.name}")
            
    elif opcion == '2':
        carpeta_logs = directorio_actual / "logs"
        
        if carpeta_logs.exists():
            print("La carpeta 'logs' ya existe.")
        else:
            carpeta_logs.mkdir()
            print("Carpeta 'logs' creada.")
            
    elif opcion == '3':
        print("Saliendo del programa.")
        break
        
    else:
        print("Opción no válida. Selecciona 1, 2 o 3.")
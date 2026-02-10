import sys
import os

if len(sys.argv) < 2:
    print("Uso: python ejercicio10.py <fichero>")
    sys.exit()

nombre_fichero = sys.argv[1]

if not os.path.exists(nombre_fichero):
    print(f"Error: El fichero '{nombre_fichero}' no se encuentra.")
else:
    with open(nombre_fichero, "r") as f:
        contenido = f.read()
        f.seek(0)
        lineas = f.readlines()
        palabras = contenido.split()
        
    print(f"Líneas: {len(lineas)}")
    print(f"Palabras: {len(palabras)}")
    print(f"Caracteres: {len(contenido)}")
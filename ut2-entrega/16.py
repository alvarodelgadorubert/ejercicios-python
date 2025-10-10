frase = input("Escribe una frase: ")

# Reemplazar vocales con asteriscos
frase_modificada = frase
for vocal in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ':
    frase_modificada = frase_modificada.replace(vocal, '*')

print(f"Frase original: {frase}")
print(f"Frase modificada: {frase_modificada}")
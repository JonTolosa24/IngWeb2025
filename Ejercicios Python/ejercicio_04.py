print("Introduce la posición de inicio: ")
posicion = input()

print("Introduce la longitud del substring: ")
longitud = input()

frase = input("Introduce una frase: ")

substring = frase[posicion:posicion + longitud]

print("Resultado:", f'"{substring}"')

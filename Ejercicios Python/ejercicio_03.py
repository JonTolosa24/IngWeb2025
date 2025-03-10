texto = input("Introduce un texto: ")

if len(texto) < 3:
    print("El texto debe tener al menos 3 caracteres.")
else:
    resultado = texto[:3] + texto[-3:]
    print("Resultado:", resultado)


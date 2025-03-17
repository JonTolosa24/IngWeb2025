numeros = []

while True:
    entrada = input("Introduce un número (o 'fin' para terminar): ")

    if entrada.lower() == "fin":
        break
    
    numeros.append(int(entrada))

if numeros:
    print("El número más alto es:", max(numeros))
else:
    print("No se introdujeron números.")
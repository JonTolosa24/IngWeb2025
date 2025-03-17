lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
frecuencia = {}

for num in lista:
    if num in frecuencia:
        frecuencia[num] += 1
    else:
        frecuencia[num] = 1

print(frecuencia)

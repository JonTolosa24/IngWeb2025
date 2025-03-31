estudiantes = [
 {"nombre": "Carlos", "notas": [7, 4, 8, 3]},
 {"nombre": "Ana", "notas": [5, 6, 4, 9]},
 {"nombre": "Luis", "notas": [3, 2, 1, 4]},
 {"nombre": "María", "notas": [6, 8, 7, 9]},
]

def contar_suspensos(notas):
    contador = 0
    
    for nota in notas:
        if nota < 5:
            contador += 1
    return contador
    

def clasifica(notas):
    notas_mayores = notas[0]
    notas_menores = notas[0]
    
    for nota in notas:
        if nota > notas_mayores:
            notas_mayores = nota
        elif nota < notas_menores:
            notas_menores = nota
    return notas_mayores, notas_menores
    
    print(notas_menores, notas_mayores)



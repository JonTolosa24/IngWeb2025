lista1 = []
lista2 = []

print("Introduce 5 números para la primera lista:")
for _ in range(5):
    lista1.append(int(input("Número: ")))

print("Introduce 5 números para la segunda lista:")
for _ in range(5):
    lista2.append(int(input("Número: ")))

numeros_comunes = list(set(lista1) & set(lista2))

print("Números en común entre ambas listas:", numeros_comunes)

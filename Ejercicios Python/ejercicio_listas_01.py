lista = [12, 23, 5, 29, 92, 64]
print("Lista inicial:", lista)

ultimo = lista.pop()
lista.insert(0, ultimo)
print(lista)

segundo = lista.pop(1)
lista.append(segundo)
print(lista)

lista.insert(0, 14)
print(lista)

suma_total = sum(lista)
lista.append(suma_total)
print(lista)

lista.extend([4, 11, 32])
print(lista)

lista = [num for num in lista if num % 2 == 0]
print(lista)

lista.sort()
print(lista)

lista.clear()
print(lista)

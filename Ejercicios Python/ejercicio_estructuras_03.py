num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num1 > num2:
    num1, num2 = num2, num1

suma_pares = 0
suma_impares = 0

contador = num1
while contador <= num2:
    if contador % 2 == 0:
        suma_pares += contador
    else:
        suma_impares += contador
    contador += 1

print(f"La suma de los números pares entre {num1} y {num2} es: {suma_pares}")
print(f"La suma de los números impares entre {num1} y {num2} es: {suma_impares}")

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num1 > num2:
    num1, num2 = num2, num1  

suma = 0

contador = num1
while contador <= num2:
    print(f"el contador va por el : {contador}")
    suma += contador
    contador += 1

print(f"La suma de los números entre {num1} y {num2} es: {suma}")

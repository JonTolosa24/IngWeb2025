from random import randint

def verificar_intento(numero_secreto, intento):
    if intento == numero_secreto:
                return "¡Felicidades! Has adivinado el número."

def juego():
    numero_secreto = randint(1, 10)
    intentos = 0
    
    print("He pensado en un número del 1 al 10. ¡Adivínalo!")
    
    while True:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1
            mensaje = verificar_intento(numero_secreto, intento)
            print(mensaje)
            if intento == numero_secreto:
                print(f"Lo lograste en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

juego()
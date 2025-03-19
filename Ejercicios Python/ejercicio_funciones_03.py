def validar_rango(numero, minimo=1, maximo=20):
    """
    Verifica si un número está dentro de un rango específico.
    :param numero: Número a verificar
    :param minimo: Límite inferior del rango (por defecto 1)
    :param maximo: Límite superior del rango (por defecto 20)
    :return: True si está en el rango, False en caso contrario
    """
    return minimo <= numero <= maximo

def esta_en_lista(numero, lista):
    """
    Verifica si un número está dentro de una lista dada.
    :param numero: Número a verificar
    :param lista: Lista de números
    :return: True si el número está en la lista, False en caso contrario
    """
    return numero in lista

def main():
    numeros_validos = [6, 14, 11, 3, 2, 1, 15, 19]
    try:
        numero = int(input("Introduce un número del 1 al 20: "))
        if validar_rango(numero):
            if esta_en_lista(numero, numeros_validos):
                print(f"El número {numero} está en la lista.")
            else:
                print(f"El número {numero} no está en la lista.")
        else:
            print("Número fuera del rango permitido.")
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")

if __name__ == "__main__":
    main()

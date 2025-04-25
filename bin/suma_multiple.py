def suma(*numeros): # * para cualquier número de argumentos, guardados en una tupla
    """
    Suma una cantidad dinámica de números.

    Args:
        números: números a sumar
    Returns:
        La suma de los n números
    """

    return sum(numeros)

print(suma(1, 2, 3)) # 3 argumentos
print(suma(7, 1, 85, 3, 12)) # 5 argumentos
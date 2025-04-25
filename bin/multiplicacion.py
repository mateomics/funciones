def multiplicar(a, b):
    """
    Multiplica los valores a y b.

    Args:
        a: Primer valor
        b: Segundo valor
    Returns:
        Producto de a y b
    """

    return a * b

a = int(input('Ingrese el primer número: ')) # Casteo a int
b = int(input('Ingrese el segundo número: '))
c = multiplicar(a, b)
print(c)
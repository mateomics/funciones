def contar_nucleotidos(secuencia):
    """
    Cuenta el número de cada nucleótido en una secuencia dada.

    Args:
        secuencia: Secuencia a analizar
    Returns:
        Diccionario con el conteo de cada nucleótido (A, C, G, T)
    """

    bases = 'ACGT'
    num_bases = {} # Inicializa un diccionario para contar los nucleótidos
    for base in bases:
        num_bases[base] = secuencia.upper().count(base)

    return num_bases
        
secuencia = 'ATGCGATCGATCGATCGATCGATCGATCGATCGATCG'
num_bases = contar_nucleotidos(secuencia)

for base, num_base in num_bases.items():
    print(f"El nucleotido {base} aparece {num_base} veces en la secuencia")
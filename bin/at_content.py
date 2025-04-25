def calcular_at_content(secuencia, decimales):
    """
    Calcula el contenido de AT en una secuencia dada.

    Args:
        secuencia: Secuencia a analizar
        decimales: decimales a incluir en el resultado
    Returns:
        Contenido de AT en la secuencia
    """
    
    secuencia = secuencia.upper() # Convierte la secuencia a mayúsculas para evitar problemas de case
    a_count = secuencia.count('A')
    t_count = secuencia.count('T')
    
    total_count = len(secuencia)
    if total_count == 0:
        return 0.0
    at_content = (a_count + t_count) / total_count
    return round(at_content, decimales)

at_content = calcular_at_content(decimales=3, secuencia="ATGCGATCGATCGATCGATCGATCGATCGATCGATCGATCG")
print(f"El contenido AT de la secuencia es: {at_content}")

# Test para verificar que la función calcula correctamente el contenido AT
assert calcular_at_content("AtGc", 3) == 0.4 # Falso: Assertionerror
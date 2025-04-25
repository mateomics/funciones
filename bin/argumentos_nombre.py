def mostrar_datos(**datos): # ** para cualquier número de argumentos con nombre
    """
    Relaciona n datos en un diccionario y los muestra a pantalla en formato key:value.

    Args:
        datos: Datos a mostrar, cada uno con su key y value 
    Returns:
        None
    """

    for key, value in datos.items():
        # Guardado en diccionario
        print(f"{key}: {value}")

mostrar_datos(Nombre='Anonio', Edad=18, Residencia='Chamilpa') # 3 argumentos, cada uno con su key y value
def cuenta_lineas (texto):
    cantidad_lineas = list(texto.split("\n"))
    return len(cantidad_lineas)
    #Devuelve la cantidad de lineas que tiene el texto

def cuenta_palabras (texto):
    cantidad_palabras = list(texto.split( ))
    return len(cantidad_palabras)
    #Devuelve la cantidad de palabras que tiene el texto

def calcula_promedio (texto):
    cantidad_palabras = list(texto.split( ))
    cantidad_lineas = list(texto.split("\n"))
    palabras = len(cantidad_palabras)
    lineas = len(cantidad_lineas)
    promedio = palabras / lineas
    return promedio
    #Calcula el promedio de palabras por linea

def mas_lineas_que_promedio (texto):
    cantidad_lineas = list(texto.split("\n"))
    promedio = calcula_promedio(texto)
    palabras_por_linea = {}
    print (f"Lineas por encima del promedio: {round(promedio, 2)}")
    for elem in cantidad_lineas:
        palabras_por_linea[elem] = len(elem.split())
        if palabras_por_linea[elem] > promedio:
            print (f"{elem} ({palabras_por_linea[elem]} palabras)")
    #Imprime las lineas que tienen más palabras que el promedio (con su cantidad)
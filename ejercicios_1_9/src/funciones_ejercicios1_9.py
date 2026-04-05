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

def pasar_a_segundos (duracion):
   minutos, segundos = duracion.split(":")
   total = int(minutos) * 60 + int(segundos)
   return total
    #Convienrte una duración m:ss a segundos para poder operar

def pasar_a_minutos (total_segundos):
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return minutos, segundos
    #Convierte una cantidad de segundos al formato m:ss para mostrar el resultado

def duracion_total (playlist):
    total = 0
    for cancion in playlist:
        duracion = cancion["duration"]
        total += pasar_a_segundos(duracion)
    return total
    #Calcula la duracion total de la playlist sumando la duracion de cada cancion

def cancion_mas_larga(playlist):
    max_cancion = None
    max_duracion = 0
    for cancion in playlist:
        dur = pasar_a_segundos(cancion["duration"])
        if dur > max_duracion:
            max_duracion = dur
            max_cancion = cancion
    return max_cancion
    #Devuelve la cancion mas larga de una playlist

def cancion_mas_corta(playlist):
    min_cancion = None
    min_duracion = float('inf')
    for cancion in playlist:
        dur = pasar_a_segundos(cancion["duration"])
        if dur < min_duracion:
            min_duracion = dur
            min_cancion = cancion
    return min_cancion
    #Devuelve la cancion mas corta de una playlist

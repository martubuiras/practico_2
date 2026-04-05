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

def tiene_un_arroba(email):
    if email.count("@") == 1:
        return True
    else:
        return False
    #Devuelve True si el email tiene un solo arroba, False en caso contrario

def tiene_texto_antes_del_arroba (email):
    partes = email.split ("@")
    if len(partes[0]) > 0:
        return True
    else:
        return False
    #Devuelve True si el email tiene texto antes del arroba, False en caso contrario

def tiene_punto_despues_del_arroba (email):
    partes = email.split("@")
    if len(partes) != 2:
        return False
    else:
        if "." in partes[1]:
            return True
        else:
            return False
    #Devuelve True si el email tiene un punto después del arroba, False en caso contrario

def no_empieza_ni_termina_mal(email):
    if not (email.startswith("@") or email.endswith("@") or email.startswith("..") or email.endswith("..")):
        return True
    else:
        return False
    #Devuelve True si el email no empieza ni termina con un arroba o dos puntos

def dominio_valido(email):
    partes = email.split(".")
    if len(partes) < 2:
        return False
    else:
        if len(partes[-1]) >= 2:
            return True
        else:
            return False
    #Devuelve True si el email tiene un dominio con al menos 2 caracteres

def es_email_valido(email):
    if (
        tiene_un_arroba(email) and
        tiene_texto_antes_del_arroba(email) and
        tiene_punto_despues_del_arroba(email) and
        no_empieza_ni_termina_mal(email) and
        dominio_valido(email)
    ):
        return True
    else:
        return False
    #Devuelve True si el email cumple con todas las condiciones para ser válido

def nombre_valido (name):
    if (name is not None) and (name.strip() != ""):
        return True
    else:
        return False
    #Devuelve True si el nombre no es None ni una cadena vacía

def nota_valida (grade):
    if grade is None or grade == "":
        return False
    else:
        if grade.isdigit():
            return True
        else:
            return False
    #Devuelve True si la nota es un número 

def normalizar_registro(student):
    nombre = student["name"].strip().title()
    estado = student["status"].strip().title()
    nota = int(student["grade"])
    return {"name": nombre, "grade": nota, "status": estado}
    #Normaliza el registro poniendo el nombre y estado en formato titulo y convirtiendo la nota a un número entero

def eliminar_duplicados(lista):
    resultado = {}
    for alumno in lista:
        nombre = alumno["name"]
        if nombre not in resultado:
            resultado[nombre] = alumno
        else:
            if alumno["grade"] > resultado[nombre]["grade"]:
                resultado[nombre] = alumno
    return list(resultado.values())
    #Elimina los duplicados quedandose con la nota más alta

    
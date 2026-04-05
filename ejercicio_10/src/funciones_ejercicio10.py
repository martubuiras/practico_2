def sumar_puntaje (jueces):
    return sum(jueces.values())
       
def actualizar_resultados (resultados, nombre, suma):    
    resultados[nombre]['total'] += suma
    #Actualiza el total de puntajes por cada participante 

    if suma > resultados[nombre]['mejor']:
        resultados[nombre]['mejor'] = suma
        #Actualiza el mejor puntaje de cada participante

def procesar_ronda (ronda, resultados):
    puntajes_ronda = {}
    #Crea una lista vacía para ir completando con los puntajes de cada jugador
    for nombre, jueces in ronda ['scores'].items():
        suma = sumar_puntaje(jueces)
        puntajes_ronda[nombre] = suma
        actualizar_resultados(resultados, nombre, suma)
        
    ganador = max(puntajes_ronda, key=puntajes_ronda.get)
    #Busco el participante con mayor puntaje en esa ronda

    resultados[ganador]["ganadas"] += 1
    #Le agrego la victoria al ganador

    return puntajes_ronda, ganador

def mostrar_tabla_parcial (resultados):
    for nombre, datos in resultados.items():
        print (f"{nombre:<12}{datos['total']:<15}")
        #Imprime los puntajes de cada participante 

def mostrar_tabla_final (resultados, ronda):
    ordenados = sorted(resultados.items(), key=lambda x: x[1]['total'], reverse=True)
    #Ordena a los participantes de mayor a menor segun su puntaje

    print ("\nTabla final:")
     # Encabezado
    print(f"{'Cocinero':<12}{'Puntaje':<10}{'Rondas ganadas':<18}{'Mejor ronda':<15}{'Promedio':<10}")
    print("-" * 65)

    for nombre, datos in ordenados:
        promedio = datos['total'] / len(ronda)
        print(f"{nombre:<12}{datos['total']:<10}{datos['ganadas']:<18}{datos['mejor']:<15}{promedio:<10.1f}")
    #Imprime la tabla final con el promedio redoneado a un decimal

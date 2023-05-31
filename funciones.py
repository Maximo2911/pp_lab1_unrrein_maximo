import json
import re
from validaciones import *
#funcion para json
def abrir_leer_json(url:str):                                               #* BIEN
    '''
    Esta funcion abre un archivo json y lee su contenido
    Recibe la ruta de acceso al archivo json
    Retorna el contenido json
    '''
    with open(url, "r") as archivo:
            contenido = archivo.read()
            lista_archivo = json.loads(contenido)
    return lista_archivo

lista_archivo = abrir_leer_json("W:\segundo_parcial\pp_lab1_unrrein_maximo\dt.json")

def mostrar_indices()->str:
    indice = 0
    mensaje = ""
    for diccionarios_jugadores in lista_archivo["jugadores"]:
        nombre = diccionarios_jugadores["nombre"]
        posicion = diccionarios_jugadores["posicion"]
        mensaje += f"{indice}) {nombre} -- {posicion}\n"
        indice += 1
    return mensaje
# print(mostrar_indices())

#punto 1 
def mostrar_nombre_posicion(lista_archivo:dict)->str:                           #* BIEN
    '''
    Esta funcion muestra los jugadores y su posicion
    Toma como dato la url del archivo con los jugadores(url = ruta de acceso)
    Retorna un los jugadores con su respectiva posicion
    '''
    mensaje_retorno = ""
    for diccionarios_jugadores in lista_archivo["jugadores"]:
        nombre = diccionarios_jugadores["nombre"]
        posicion = diccionarios_jugadores["posicion"]
        mensaje_retorno += f"{nombre} -- {posicion}\n"

    mensaje_retorno = mensaje_retorno[:-1]
    return mensaje_retorno
# print(mostrar_nombre_posicion(lista_archivo))

#punto 2
def mostrar_estadisticas_jugadores(lista_archivo:dict, numero_ingresado:int)->str: #* BIEN
    '''
    Esta funcion muestra las estadisticas del jugador seleccionado
    Toma como dato la lista json y un numero entero dato por el usuario, que sera el indice que seleccionará el jugador
    Retorna un mensaje con las estadisticas del jugador seleccionado
    '''
    mensaje_retorno = ""
    # indice_elegido = int(input("Ingrese el indice del jugador:"))
    
    lista_jugador = lista_archivo["jugadores"][numero_ingresado]
    print(lista_jugador["nombre"])
    print(lista_jugador["posicion"])
    for datos in lista_jugador["estadisticas"]:
        valor = lista_jugador["estadisticas"][datos]
        mensaje_retorno += f'{datos}: {valor}\n'
    mensaje_retorno = mensaje_retorno[:-1]
    return mensaje_retorno
# print(mostrar_estadisticas_jugadores(lista_archivo, 5))

#punto 3
def guardar_jugador_seleccionado(lista_archivo:dict, indice_jugador:int)->str:  #* Masomenos
    '''
    Guarda los datos y estadisticas de un jugador en un csv
    Recibe la lista del archivo json y el indice del jugador a guardar
    Retorna los datos y estadisticas del jugador y ademas lo guarda en un csv
    '''
    mensaje = ""
    lista_jugador = lista_archivo["jugadores"][indice_jugador]
    mensaje += f'{lista_jugador["nombre"]}\n{lista_jugador["posicion"]}\n'
    mensaje += mostrar_estadisticas_jugadores(lista_archivo, indice_jugador)
    with open("jugador_elegido.csv", "w+") as archivo:
        archivo.write(mensaje)
    return mensaje
# print(guardar_jugador_seleccionado(lista_archivo, 3))

#punto 4
def buscar_jugador_logros(lista_archivo:dict, nombre_jugador:str)->str:         #*BIEN
    '''
    Busca jugador y muestra logros
    Recibe lista json y nombre del jugador a buscar
    Retorna los logros del jugador
    '''
    mensaje = ""
    # validar_nombre(nombre_jugador)
    if not validar_nombre(nombre_jugador) == None:
        for diccionario in lista_archivo["jugadores"]:
            nombre_jugador = validar_nombre(nombre_jugador)
            if nombre_jugador in diccionario["nombre"]:
                mensaje += f'{nombre_jugador}\n' 
                for keys in diccionario["logros"]:
                    mensaje += f'{keys}\n'
        mensaje = mensaje[:-1]
        mensaje = mensaje.rstrip("\n") #Eliminar la última línea en blanco si existe
        return mensaje
    else:
        return "[ERROR] No es un nombre valido"
    
# print(buscar_jugador_logros(lista_archivo, "karl malone"))

#punto 5
def  calcular_mostrar_promedio(lista_archivo:dict)->str:                     #* BIEN
    '''
    Funcion que muestra promedios de jugadores ordenados alfabeticamente
    Toma lista del json como dato
    Retorna un mensaje string que contiene la informacion deseada
    '''
    lista_nombres = []
    lista_promedios = []
    flag_iteracion = True
    mensaje = ""
    lista_frases = []
    lista_letras = []

    for diccionario_jugadores in lista_archivo["jugadores"]:
        nombre = diccionario_jugadores["nombre"]
        lista_nombres.append(nombre)
        promedio = diccionario_jugadores["estadisticas"]["promedio_puntos_por_partido"]
        lista_promedios.append(promedio)
    longitud = len(lista_promedios)
    
    while flag_iteracion:
            flag_iteracion = False
            for indice in range(longitud - 1):
                if lista_promedios[indice] > lista_promedios[indice + 1]:
                    # aux = lista[indice]["fuerza"]
                    lista_promedios[indice + 1], lista_promedios[indice] = lista_promedios[indice], lista_promedios[indice + 1]
                    lista_nombres[indice + 1], lista_nombres[indice] = lista_nombres[indice], lista_nombres[indice + 1] 
                    flag_iteracion = True
    for indice in range(longitud):
        mensaje = f'{lista_nombres[indice]} -- Promedio: {lista_promedios[indice]}'
        lista_frases.append(mensaje)
        lista_letras.append(mensaje[:10])
    
    longitud = len(lista_letras)
    flag = True
    while flag:
        flag = False
        for indice in range(longitud - 1):
            if lista_letras[indice] > lista_letras[indice + 1]:
                lista_letras[indice + 1], lista_letras[indice] = lista_letras[indice], lista_letras[indice + 1]
                lista_frases[indice + 1], lista_frases[indice] = lista_frases[indice], lista_frases[indice + 1] 
                flag = True
    retorno = ""
    for frases in lista_frases:
        retorno += f'{frases}\n'
    retorno = retorno[:-1]
        
    return retorno
# print(calcular_mostrar_promedio(lista_archivo))

#Punto 6
def confirmar_jugador(lista_archivo:dict, nombre_jugador:str)-> str:              #* BIEN
    '''
    Funcion que confirma si el jugador estuvó en el salon de la fama
    Recibe como dato la lista del json y el nombre del jugador a buscar
    Retorna un mensaje confirmando o negando la presencia del jugador en el salon de la fama
    '''
    lista_nombres = []
    nombre_jugador = validar_nombre(nombre_jugador)
    for diccionarios in lista_archivo["jugadores"]:
        nombre = diccionarios["nombre"]
        lista_nombres.append(nombre)
    if nombre_jugador in lista_nombres:
        mensaje = "Está en el salon de la fama"
    else:
        mensaje = "No pertenece al salon de la fama"
    return mensaje
# print(confirmar_jugador(lista_archivo, "michael jordan"))

#Punto 7
def mostrar_jugador_mayor_rebotes(lista_archivo:dict)->str:                            #* BIEN
    '''
    Funcion que muestra el jugador con la mayor cantidad de rebotes totales realizados
    Recibe como dato la lista json
    Retorna mensaje que muestra el jugador buscado
    '''
    lista_archivo = abrir_leer_json("W:\segundo_parcial\pp_lab1_unrrein_maximo\dt.json")
    max_promedio_rebotes = 0
    nombre_jugador = ""
    
    for diccionarios in lista_archivo["jugadores"]:
        promedio_jugador = diccionarios["estadisticas"]["rebotes_totales"]
        if max_promedio_rebotes < promedio_jugador:
            max_promedio_rebotes = promedio_jugador
            nombre_jugador = diccionarios["nombre"]
    mensaje = f'El jugador con mayor cantidad de rebotes es: {nombre_jugador} con {max_promedio_rebotes}'
    return mensaje
# print(mostrar_jugador_mayor_rebotes(lista_archivo)) 

#Punto 8
def mostrar_jugador_mayor_tiros(lista_archivo:dict)->str: #mayor porcentaje de tiros de campo #* BIEN 
    '''
    Funcion que muestra el jugador con la mayor porcentaje de tiros totales realizados
    Recibe como dato la lista json
    Retorna mensaje que muestra el jugador buscado
    '''
    max_porcentaje_tiros_de_campo = 0
    nombre_jugador = ""
    
    for diccionarios in lista_archivo["jugadores"]:
        porcentaje_jugador = diccionarios["estadisticas"]["porcentaje_tiros_de_campo"]
        if max_porcentaje_tiros_de_campo < porcentaje_jugador:
            max_porcentaje_tiros_de_campo = porcentaje_jugador
            nombre_jugador = diccionarios["nombre"]
    mensaje = f'El jugador con mayor porcentaje de tiros de campo es: {nombre_jugador} con {max_porcentaje_tiros_de_campo}'
    return mensaje
# print(mostrar_jugador_mayor_tiros(lista_archivo))

#Punto 9
def mostrar_jugador_mayor_asistencias(lista_archivo:dict)->str: #mayor cantidad de asistencias totales. #* BIEN
    '''
    Funcion que muestra el jugador con la mayor cantidad de asistencias totales realizados
    Recibe como dato la lista json
    Retorna mensaje que muestra el jugador buscado
    '''
    max_asistencias = 0
    nombre_jugador = ""
    
    for diccionarios in lista_archivo["jugadores"]:
        porcentaje_jugador = diccionarios["estadisticas"]["asistencias_totales"]
        if max_asistencias < porcentaje_jugador:
            max_asistencias = porcentaje_jugador
            nombre_jugador = diccionarios["nombre"]
    mensaje = f'El jugador con mayor asistencias es: {nombre_jugador} con {max_asistencias}'
    return mensaje
# print(mostrar_jugador_mayor_asistencias(lista_archivo))

#Punto 10
def valor_jugador_mayor_promedio_puntos_partidos(lista_archivo:dict, numero_ingresado:int)->str:
    '''
    Muestra jugadores que promediaron mas puntos que el numero ingresado 
    Recibe como dato la lista json y toma el numero ingresado que luego usará como referencia para evaluar
    Retorna mensaje con jugadores que promediaron mas puntos que el numero ingresado 
    '''
    # acumular_valor = 0
    nombre_jugador = ""
    puntos_partidos = 0
    mensaje = ""
    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        puntos_partidos = diccionarios["estadisticas"]["promedio_puntos_por_partido"]
        if numero_ingresado < puntos_partidos:
            nombre_jugador = diccionarios["nombre"]
            mensaje += f'Nombre: {nombre_jugador} -- Promedio puntos por partido: {puntos_partidos}\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(valor_jugador_mayor_promedio_puntos_partidos(lista_archivo, 24))

#Punto 11
def valor_jugadores_mayor_promediado_rebotes(lista_archivo:dict, numero_ingresado:int)->str:              #* BIEN
    '''
    Muestra jugadores que promediaron mas rebotes que el numero ingresado 
    Recibe como dato la lista json y toma el numero ingresado que luego usará como referencia para evaluar
    Retorna mensaje con jugadores que promediaron mas rebotes que el numero ingresado
    '''
    nombre_jugador = ""
    rebote_jugadores = 0
    mensaje = ""
    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        rebote_jugadores = diccionarios["estadisticas"]["promedio_rebotes_por_partido"]
        if numero_ingresado < rebote_jugadores:
            nombre_jugador = diccionarios["nombre"]
            mensaje += f'Nombre: {nombre_jugador} -- Promedio rebotes por partido: {rebote_jugadores}\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(valor_jugadores_mayor_promediado_rebotes(lista_archivo, 5))

#Punto 12
def valor_jugadores_mayor_promediado_asistencias(lista_archivo:dict, numero_ingresado:int)->str:      #* BIEN
    '''
    Muestra jugadores que promediaron mas asistencias que el numero ingresado 
    Recibe como dato la lista json y toma el numero ingresado que luego usará como referencia para evaluar
    Retorna mensaje con jugadores que promediaron mas asistencias que el numero ingresado
    '''
    nombre_jugador = ""
    asistencia_jugadores = 0
    mensaje = ""
    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        asistencia_jugadores = diccionarios["estadisticas"]["promedio_asistencias_por_partido"]
        if numero_ingresado < asistencia_jugadores:
            nombre_jugador = diccionarios["nombre"]
            mensaje += f'Nombre: {nombre_jugador} -- Promedio asistencia por partido: {asistencia_jugadores}\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(valor_jugadores_mayor_promediado_asistencias(lista_archivo, 6))

#Punto 13
def jugador_mayor_cantidad_robos(lista_archivo:dict)->str:                  #* BIEN
    '''
    Funcion que devuelve jugador con mas cantidad de robos
    Recibe como dato la lista json
    Retorna mensaje que muestra al jugador buscado
    '''
    max_robos = 0
    nombre_jugador = ""
    
    for diccionarios in lista_archivo["jugadores"]:
        # print(max_robos)
        porcentaje_jugador = diccionarios["estadisticas"]["robos_totales"]
        if max_robos < porcentaje_jugador:
            max_robos = porcentaje_jugador
            nombre_jugador = diccionarios["nombre"]
    mensaje = f'El jugador con mas robos totales es: {nombre_jugador} con {max_robos}'
    return mensaje
# print(jugador_mayor_cantidad_robos(lista_archivo))

#Punto 14
def jugador_mayor_cantidad_bloqueos_totales(lista_archivo:dict)->str:           #* BIEN
    '''
    Funcion que compara y devuelve el jugador con mas cantidad de bloqueos totales
    Recibe como dato la lista json
    Retorna mensaje que muestra al jugador buscado
    '''
    max_bloqueos = 0
    nombre_jugador = ""
    
    for diccionarios in lista_archivo["jugadores"]:
        porcentaje_jugador = diccionarios["estadisticas"]["bloqueos_totales"]
        if max_bloqueos < porcentaje_jugador:
            max_bloqueos = porcentaje_jugador
            nombre_jugador = diccionarios["nombre"]
    mensaje = f'El jugador con mas bloqueos totales es: {nombre_jugador} con {max_bloqueos}'
    return mensaje
# print(jugador_mayor_cantidad_bloqueos_totales(lista_archivo))

#Punto 15
def valor_mayor_promediado_tiros_libres(lista_archivo:dict, numero_ingresado:int)->str:         #* BIEN
    '''
    Muestra jugadores que promediaron mas tiros libres que el numero ingresado 
    Recibe como dato la lista json y toma el numero ingresado que luego usará como referencia para evaluar
    Retorna mensaje con jugadores que promediaron mas tiros libres que el numero ingresado
    '''
    nombre_jugador = ""
    tiros_libres_jugadores = 0
    mensaje = ""
    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        tiros_libres_jugadores = diccionarios["estadisticas"]["porcentaje_tiros_libres"]
        if numero_ingresado < tiros_libres_jugadores:
            nombre_jugador = diccionarios["nombre"]
            mensaje += f'Nombre: {nombre_jugador} -- Promedio tiros libres: {tiros_libres_jugadores}\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(valor_mayor_promediado_tiros_libres(lista_archivo, 50))

#Punto 16                               
def mostrar_promedio_puntos_equipo(lista_archivo:dict)->str:                                    #* BIEN
    '''
    Funcion que muestra los nombres y promedio de puntos de cada uno, excluyendo el que menor promedio tenga
    Recibe como dato la lista json
    Retorna mensaje con jugadores que promediaron mas puntos menos el ultimo
    '''
    nombre_jugador = ""
    puntos_jugadores = 0
    mensaje = ""
    lista_nombres = []
    lista_puntos = []
    flag_iteracion = True

    longitud = len(lista_archivo["jugadores"])
    for diccionarios in lista_archivo["jugadores"]:
        nombre_jugador = diccionarios["nombre"]
        puntos_jugadores = diccionarios["estadisticas"]["promedio_puntos_por_partido"]
        lista_nombres.append(nombre_jugador)
        lista_puntos.append(puntos_jugadores)
    while flag_iteracion:
            flag_iteracion = False
            for indice in range(longitud - 1):
                if lista_puntos[indice] < lista_puntos[indice + 1]:
                    # aux = lista[indice]["fuerza"]
                    lista_puntos[indice + 1], lista_puntos[indice] = lista_puntos[indice], lista_puntos[indice + 1]
                    lista_nombres[indice + 1], lista_nombres[indice] = lista_nombres[indice], lista_nombres[indice + 1] 
                    flag_iteracion = True
    
    for indice in range(longitud - 1):
        nombre = lista_nombres[indice]
        puntos = lista_puntos[indice]
        mensaje += f'Nombre: {nombre} -- Promedio puntos por partido: {puntos}\n' 
    mensaje = mensaje[:-1]
    return mensaje
# print(mostrar_promedio_puntos_equipo(lista_archivo))

#Punto 17
def mostrar_jugador_mayor_logros(lista_archivo:dict)->str:              #* BIEN
    '''
    Funcion que muestra el jugador con mas logros
    Recibe como dato la lista json
    Retorna mensaje con el jugador con mas logros obtenidos
    ''' 
    patron = r'^(\d+)'
    lista_logros = []
    lista_nombres = []
    flag_iteracion = True
    for diccionarios in lista_archivo["jugadores"]:
        cantidad  = 0
        nombre = diccionarios["nombre"]
        lista_nombres.append(nombre)
        for logros in diccionarios["logros"]:
            match = re.search(patron, logros)
            if match:
                cantidad += int(match.group(1))
            else:
                cantidad += 1
        lista_logros.append(cantidad)
        
    longitud = len(lista_logros)
    while flag_iteracion:
            flag_iteracion = False
            for indice in range(longitud - 1):
                if lista_logros[indice] < lista_logros[indice + 1]:
                    lista_logros[indice + 1], lista_logros[indice] = lista_logros[indice], lista_logros[indice + 1]
                    lista_nombres[indice + 1], lista_nombres[indice] = lista_nombres[indice], lista_nombres[indice + 1] 
                    flag_iteracion = True
    mensaje = f"El jugador {lista_nombres[0]} es el que mas logros tiene: {lista_logros[0]}"
    return mensaje
# print(mostrar_jugador_mayor_logros(lista_archivo))

#Punto 18
def valor_mayor_promediado_tiros_triples(lista_archivo:dict, numero_ingresado:int)->str:            #* BIEN
    '''
    Muestra jugadores que promediaron mas tiros triples que el numero ingresado
    Recibe como dato la lista json y el numero ingresado que luego usara como referencia para evaluar
    Retorna jugadores que promediaron mas tiros triples que el numero ingresado
    '''
    nombre_jugador = ""
    tiros_triples_jugadores = 0
    mensaje = ""
    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        tiros_triples_jugadores = diccionarios["estadisticas"]["porcentaje_tiros_triples"]
        if numero_ingresado < tiros_triples_jugadores:
            nombre_jugador = diccionarios["nombre"]
            mensaje += f'Nombre: {nombre_jugador} -- Promedio tiros triples: {tiros_triples_jugadores}\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(valor_mayor_promediado_tiros_triples(lista_archivo, 38))

#Punto 19
def mostrar_jugador_mas_temporadas(lista_archivo:dict)->str:                #* BIEN
    '''
    Funcion que muestra el jugador con mas temporadas
    Recibe como dato la lista json
    Retorna mensaje con el jugador con mas temporadas obtenidos
    '''
    nombre_jugador = ""
    temporadas = 0
    mensaje = ""
    lista_nombres = []
    lista_temporadas = []
    flag_iteracion = True
    
    longitud = len(lista_archivo["jugadores"])
    
    for diccionarios in lista_archivo["jugadores"]:
        nombre_jugador = diccionarios["nombre"]
        temporadas = diccionarios["estadisticas"]["temporadas"]
        lista_nombres.append(nombre_jugador)
        lista_temporadas.append(temporadas)
    while flag_iteracion:
            flag_iteracion = False
            for indice in range(longitud - 1):
                if lista_temporadas[indice] < lista_temporadas[indice + 1]:
                    lista_temporadas[indice + 1], lista_temporadas[indice] = lista_temporadas[indice], lista_temporadas[indice + 1]
                    lista_nombres[indice + 1], lista_nombres[indice] = lista_nombres[indice], lista_nombres[indice + 1] 
                    flag_iteracion = True
    
    mensaje = f"El jugador con mas temporadas es {lista_nombres[0]} con {lista_temporadas[0]}" 
    return mensaje
# print(mostrar_jugador_mas_temporadas(lista_archivo))

#Punto 20
def jugadores_ordenados_superan_valor(lista_archivo:dict, numero_ingresado:int): #porcentaje de tiros de campo superior a ese valor
    '''
    Funcion que ordena los jugadores por posicion, que superan el valor ingresado
    Recibe como dato la lista json y el numero ingresado que luego usara como referencia para evaluar
    Retorna mensaje con el jugador con mas temporadas jugadas
    '''
    nombre_jugador = ""
    tiros_de_campo = 0
    mensaje = ""
    lista_base = []
    lista_escolta = []
    lista_alero = []
    lista_ala_pivot = []
    lista_pivot = []
    lista_global = []

    for diccionarios in lista_archivo["jugadores"]:
        # print(f'{numero_ingresado} < {numero_ingresado}')
        tiros_de_campo = diccionarios["estadisticas"]["porcentaje_tiros_de_campo"]
        if numero_ingresado < tiros_de_campo:
            nombre_jugador = diccionarios["nombre"]
            posicion = diccionarios["posicion"]
            # print(posicion)
            mensaje = f'Nombre: {nombre_jugador} -- Posicion: {posicion} -- Promedio tiros de campo: {tiros_de_campo}'
        
        match posicion:
            case "Base":
                lista_base.append(mensaje)
            case "Escolta":
                lista_escolta.append(mensaje)
            case "Alero":
                lista_alero.append(mensaje)
            case "Ala-Pivot":
                lista_ala_pivot.append(mensaje)
            case "Pivot":
                lista_pivot.append(mensaje)
    
    lista_global.append(lista_base)
    lista_global.append(lista_escolta)
    lista_global.append(lista_alero)
    lista_global.append(lista_ala_pivot)
    lista_global.append(lista_pivot)
    # print(lista_global)
    mensaje = mensaje[:-1]
    '''
    (1) Base.
    (2) Escolta.
    (3) Alero.
    (4) Ala-pívot.
    (5) Pívot.
    '''
    for listas in lista_global:
        # print(listas)
        longitud = len(listas)
        if longitud > 1:
            for indice in range(longitud):
                print(listas[indice])
        else:
            print(listas[0])
# print(jugadores_ordenados_superan_valor(lista_archivo, 40))

#Punto 23
def calcular_posicion_jugador(lista_archivo:dict)->str:
    '''
    Funcion que ordena alfabeticamente los jugadores con la posicion que ocupan en cada estadistica(Puntos | Rebotes | Asistencias | Robos)
    Recibe como dato la lista json
    Retorna "tabla" con los jugadores con la respetiva posicion que ocupan en las estadisticas
    '''
    
    lista_puntos_totales = []
    lista_rebotes_totales = []
    lista_robos_totales = []
    
    '''
    puntos_totales
    rebotes_totales
    asistencias_totales
    robos_totales
    '''

    def ordenamiento_listas(key:str):
        flag_iteracion = True
        lista = []
        lista_nombre = []
        if key == "nombre":
            for diccionarios in lista_archivo["jugadores"]:
                nombre = diccionarios["nombre"]
                lista_nombre.append(nombre)
                longitud = len(lista_nombre)
                flag = True
                while flag:
                    flag = False
                    for indice in range(longitud - 1):
                        if lista_nombre[indice] > lista_nombre[indice + 1]:
                            lista_nombre[indice + 1], lista_nombre[indice] = lista_nombre[indice], lista_nombre[indice + 1]
                            flag = True
        else: 
            for diccionarios in lista_archivo["jugadores"]:
            # print(f'{numero_ingresado} < {numero_ingresado}')
                valor_lista = diccionarios["estadisticas"][key]
                nombre = diccionarios["nombre"]
                lista.append(valor_lista)
                lista_nombre.append(nombre)
            # print(lista_nombre)
            longitud = len(lista)
            while flag_iteracion:
                flag_iteracion = False
                for indice in range(longitud - 1):
                    if lista[indice] < lista[indice + 1]:
                        # aux = lista[indice]["fuerza"]
                        lista[indice + 1], lista[indice] = lista[indice], lista[indice + 1]
                        lista_nombre[indice + 1], lista_nombre[indice] = lista_nombre[indice], lista_nombre[indice + 1] 
                        flag_iteracion = True
        return lista_nombre
    
    lista_puntos_totales = ordenamiento_listas("puntos_totales")
    lista_rebotes_totales = ordenamiento_listas("rebotes_totales")
    lista_asistencias_totales = ordenamiento_listas("asistencias_totales")
    lista_robos_totales = ordenamiento_listas("robos_totales")
    lista_nombres_alfabeticamente = ordenamiento_listas("nombre")
    
    encabezado = "Jugadores | Puntos | Rebotes | Asistencias | Robos\n"
    contenido = ""
    longitud = len(lista_nombres_alfabeticamente)
    for indice in range(longitud):
        contenido += f'{lista_nombres_alfabeticamente[indice]}|{1+lista_puntos_totales.index(lista_nombres_alfabeticamente[indice])}|'\
                    f'{1+lista_rebotes_totales.index(lista_nombres_alfabeticamente[indice])}|'\
                    f'{1+lista_asistencias_totales.index(lista_nombres_alfabeticamente[indice])}|'\
                    f'{1+lista_robos_totales.index(lista_nombres_alfabeticamente[indice])}\n'
        resultado = "".join([encabezado, contenido])

    with open("caracteristicas_dream_team.csv", "w+") as archivo_dream_team:
        archivo_dream_team.write(resultado)
    
    return resultado
# print(calcular_posicion_jugador(lista_archivo))

#Punto extra:
def determinar_cantidad_posiciones(diccionario_general:dict)->str:
    '''
    Funcion que recorre la lista de cada jugador y guarda su posicion para luego mostrar cant total de personas por c/d posicion
    Recibe como dato el diccionario que contiene a los jugadores con sus estadisticas
    Retorna un mensaje con las posiciones y cant de personas por cada una 
    '''
    diccionario_posiciones = {}
    flag_primera_base = True
    flag_primer_alero = True
    flag_primer_ala_pivot = True
    flag_primera_escolta = True
    mensaje = ""

    for diccionarios_jugadores in diccionario_general["jugadores"]:
        posicion = diccionarios_jugadores["posicion"]
        
        match posicion:
            case "Base":
                if flag_primera_base:
                    diccionario_posiciones["Base"] = 1
                    flag_primera_base = False
                else:
                    diccionario_posiciones["Base"] += 1
            case "Alero":
                if flag_primer_alero:
                    diccionario_posiciones["Alero"] = 1
                    flag_primer_alero = False
                else:
                    diccionario_posiciones["Alero"] += 1
            case "Ala-Pivot":
                if flag_primer_ala_pivot:
                    diccionario_posiciones["Ala-Pivot"] = 1
                    flag_primer_ala_pivot = False
                else:
                    diccionario_posiciones["Ala-Pivot"] += 1
            case "Escolta":
                if flag_primera_escolta:
                    diccionario_posiciones["Escolta"] = 1
                    flag_primera_escolta = False
                else:
                    diccionario_posiciones["Escolta"] += 1
    
    # print(diccionario_posiciones)
    for posiciones in diccionario_posiciones:
        posicion_mensaje = posiciones
        cantidad_jugadores_posicion = diccionario_posiciones[posiciones]
        mensaje += f'{posicion_mensaje}: {cantidad_jugadores_posicion}\n'
        # print(mensaje)
    mensaje = mensaje[:-1]
    # print(diccionario_general)
    return mensaje

# print(determinar_cantidad_posiciones(lista_archivo))

def mostrar_allstar_jugadores(diccionario_general:dict):
    '''
    Funcion que muestra la cantidad de premios All-star que recibio cada uno
    Recibe como dato el diccionario que contiene a cada jugador con sus estadisticas
    Retorna mensaje con cada jugador y la cantidad de veces que gano el premio(all-star)
    '''
    lista_nombres = []
    lista_allstar = []
    mensaje = ""
    contador = 0
    patron = r"(\d+)\s+veces All-Star"
    for diccionarios_jugadores in diccionario_general["jugadores"]:
        
        logros = diccionarios_jugadores["logros"]
        # veces_allstar = re.search(patron, logros)
        # print(veces_allstar.group())
        
        for sentecias in logros:
            veces_allstar = re.search(patron, sentecias)
            if veces_allstar is not None:
                numero = veces_allstar.group(1)
                nombre_jugador = diccionarios_jugadores["nombre"]
                lista_nombres.append(nombre_jugador)
                lista_allstar.append(numero)
                contador += 1

        # print(nombre_jugador)
    # print(lista_nombres)
    # print(lista_allstar)

    for indice in range(contador):
        nombre = lista_nombres[indice]
        allstar = lista_allstar[indice]
        mensaje += f'{nombre}({allstar} All-Stars)\n'
    mensaje = mensaje[:-1]
    return mensaje
# print(mostrar_allstar_jugadores(lista_archivo))

estadisticas = ["Jugadores", "Puntos", "Rebotes", "Asistencias", "Robos"]
def jugador_con_mejores_stats(diccionario_general:dict)->str:
    nombres = []
    suma_digitos_sectores = []
    
    texto_estadisticas = calcular_posicion_jugador(diccionario_general)
    # print(texto_estadisticas)
    lista = texto_estadisticas.split("\n")
    lista = lista[1:]
    lista = list(filter(bool, lista))  #para filtra una lista y eliminar los elementos vacios
    patron = r'^([A-Za-z\s]+)\|'
    longitud = len(lista)
    for jugadores in lista:
        nombre = re.search(patron, jugadores)
        nombre = nombre.group(1)
        nombres.append(nombre)

        partes = jugadores.split("|")
        for digito in partes[1:]:
            suma_digitos = 0
            digito_entero = int(digito)
            suma_digitos += digito_entero
        suma_digitos_sectores.append(suma_digitos)
    # print(nombres)
    # print(suma_digitos_sectores)

    flag = True
    while flag:
        flag = False
        for indice in range(longitud - 1):
            if suma_digitos_sectores[indice] < suma_digitos_sectores[indice + 1]:
                suma_digitos_sectores[indice + 1], suma_digitos_sectores[indice] = suma_digitos_sectores[indice], suma_digitos_sectores[indice + 1]
                nombres[indice + 1], nombres[indice] = nombres[indice], nombres[indice + 1] 
                flag = True
    # print(nombres)
    # print(suma_digitos_sectores)
    mensaje = f"El jugador con mejores estadisticas en general es: {nombres[0]}"
    return mensaje
# print(jugador_con_mejores_stats(lista_archivo))

def mejores_stats_jugadores():
    print(mostrar_jugador_mayor_rebotes(lista_archivo))
    print(mostrar_jugador_mayor_tiros(lista_archivo))
    print(mostrar_jugador_mayor_asistencias(lista_archivo))
    print(jugador_mayor_cantidad_robos(lista_archivo))
    print(jugador_mayor_cantidad_bloqueos_totales(lista_archivo))
    print(mostrar_jugador_mayor_logros(lista_archivo))
    print(mostrar_jugador_mas_temporadas(lista_archivo))
    return
# print(mejores_stats_jugadores())

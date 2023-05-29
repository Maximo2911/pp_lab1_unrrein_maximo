from funciones import *
from validaciones import *

lista_archivo = abrir_leer_json("W:\segundo_parcial\pp_lab1_unrrein_maximo\dt.json")
continuar = "s"
flag = False
while continuar == "s":
    opcion = int(input("--Menu--\n"
                "1)Mostrar a los miembros del Dream Team junto a su posición.\n"
                "2)Mostrar estadisticas del jugador seleccionado, ingresando su indice.\n"
                "3)Exportar a un archivo CSV las estadisticas obtenidas en el punto 2.\n"
                "4)Ingresar el nombre de un jugador y mostrar sus logros.\n"
                "5)Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.\n"
                "6)Ingresar el nombre de un jugador y mostrar si pertenece al Salón de la Fama.\n"
                "7)Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n"
                "8)Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
                "9)Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n"
                "10)Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
                "11)Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
                "12)Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n"
                "13)Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n"
                "14)Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
                "15)Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
                "16)Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
                "17)Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
                "18)Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
                "19)Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.\n"
                "20)Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
                "23)Mostrar el ranking por cantidad de puntos, rebotes, asistencias y robos.\n"
                "Ingrese la opción: "))
    match opcion:
        case 1:
            print(mostrar_nombre_posicion(lista_archivo))
        case 2:
            print(mostrar_indices())
            numero = int(input("Ingrese el indice: "))
            # numero_puntos_tres = numero
            # print(numero)
            print(validar_numero(numero))
            if validar_numero(numero):
                print(mostrar_estadisticas_jugadores(lista_archivo, numero))
                flag = True
            else:
                print("[ERROR]. Ingresar numero valido")
        case 3:
            if flag:
                print(guardar_jugador_seleccionado(lista_archivo, numero))
            else:
                print("[ERROR]. Debes primero elegir un indice")
        case 4:
            nombre_jugador = str(input("Ingrese el nombre del jugador a buscar: "))
            print(buscar_jugador_logros(lista_archivo, nombre_jugador))
        case 5:
            print(calcular_mostrar_promedio(lista_archivo))
        case 6:
            nombre_jugador = str(input("Ingrese el nombre del jugador a buscar: "))
            print(confirmar_jugador(lista_archivo, nombre_jugador))
        case 7:
            print(mostrar_jugador_mayor_rebotes(lista_archivo))
        case 8:
            print(mostrar_jugador_mayor_tiros(lista_archivo))
        case 9:
            print(mostrar_jugador_mayor_asistencias(lista_archivo))
        case 10:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(valor_jugador_mayor_promedio_puntos_partidos(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 11:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(valor_jugadores_mayor_promediado_rebotes(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 12:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(valor_jugadores_mayor_promediado_asistencias(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 13:        
            print(jugador_mayor_cantidad_robos(lista_archivo))
        case 14:
            print(jugador_mayor_cantidad_bloqueos_totales(lista_archivo))
        case 15:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(valor_mayor_promediado_tiros_libres(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 16:
            print(mostrar_promedio_puntos_equipo(lista_archivo))
        case 17:
            print(mostrar_jugador_mayor_logros(lista_archivo))
        case 18:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(valor_mayor_promediado_tiros_triples(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 19:
            print(mostrar_jugador_mas_temporadas(lista_archivo))
        case 20:
            numero = int(input("Ingrese el numero: "))
            if validar_numero(numero):
                print(jugadores_ordenados_superan_valor(lista_archivo, numero))
            else:
                print("[ERROR] No se ha ingresado un numero")
        case 23:
            print(calcular_posicion_jugador(lista_archivo))

    continuar = input("Desea continuar(s/n):")
"""Un aventurero le entrega a usted dos listas, una contiene una serie de lugares que debe visitar (comenzando desde su hogar) hasta un destino final,
y otra lista con la distancia que debe recorrer para llegar al siguiente lugar (en kilómetros).
El aventurero le dice que irá a pie, asuma que eso corresponde a 5 km/h.
Luego el aventurero le indicará un número X (entero positivo) de horas de caminata para su travesía.

Su trabajo es crear un programa que determine si es posible lograr la travesía propuesta,
De no ser posible, que indique cuál es el último lugar que podría visitar y cuantas horas más necesita para lograr el viaje.

ej:
lugares = [‘casa’,’montaña nevada’,’lago azul’,’valle verde’]
distancia = [0, 40, 100, 40]
tiempo_caminata = 40
=> Si puede lograrlo

lugares = [‘casa’,’montaña nevada’,’lago azul’,’valle verde’]
distancia = [0, 40, 100, 40]
tiempo_caminata = 20
=> No puede lograrlo. Último destino: montaña nevada
"""

def aventurero (lista_lugares,lista_distancias,tiempo):
    suma_distancia=0
    suma_total = 0
    iteracion = 0
    verificacion = True
    distancia_final = tiempo * 5
    for recorrido in lista_distancias:
        suma_distancia += recorrido
        iteracion += 1
        if distancia_final >= suma_distancia:
            continue
        else:
            ultimo_lugar = lista_lugares[iteracion-2]
            verificacion=False
            break
    for sumas in lista_distancias:
        suma_total += sumas
    tiempo_restante = (suma_total - distancia_final)/5
    if verificacion == True:
        print("Si puede lograrlo")
    else:
        print(f"No puede lograrlo. Último destino: {ultimo_lugar}\nNecesitas {tiempo_restante} horas más para lograr el viaje ")
    

lugares1 = ["casa","montaña nevada","lago azul","valle verde"]
distancia1 = [0, 40, 100, 40]
tiempo_caminata1 = 40

lugares2 = ["casa","montaña nevada","lago azul","valle verde"]
distancia2 = [0, 40, 100, 40]
tiempo_caminata2 = 20


aventurero(lugares2,distancia2,tiempo_caminata2)
aventurero(lugares1,distancia1,tiempo_caminata1)
        





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
    suma_distancia=0 #variable para sumar distantias por tramo
    suma_total = 0 #variable para almacenar distancia total del recorrido
    iteracion = 0 #contador de iteraciones
    verificacion = True #verificación de condiciones
    distancia_final = tiempo * 5 #cálculo de la distancia que puede recorrer la persona a 5 km/h
    for recorrido in lista_distancias: #recorro la lista de distancias
        suma_distancia += recorrido #voy sumando cada distancia en cada iteración
        iteracion += 1 #conteo de iteraciones
        if distancia_final >= suma_distancia: #si la distancia total que puede recorrer la personas es mayor que la distancia acumulada, entonces que vuelva a iterar
            continue
        else: #en caso que la distancia total ya no sea mayor a la distancia acumulada
            ultimo_lugar = lista_lugares[iteracion-2] #usamos iteracion-2 ya que el programa cuenta desde el 0 y yo deseo obtener el elemento anterior al que estamos iterando
            verificacion=False #cambio la condicion de verificación a false, ya que ya no puede hacer el recorrido completo
            break #termino de iterar la lista
    for sumas in lista_distancias: #iteración para sumar el recorrido total que desea hacer la persona
        suma_total += sumas #almaceno las distancias
    tiempo_restante = (suma_total - distancia_final)/5 #calculo el tiempo que le falta por recorrer restando la distancia total del recorrido menos la distancia que puede recorrer la persona en el tiempo dado
    if verificacion == True: #condiciones de si puede lograrlo o no
        print("Si puede lograrlo")
    else:
        print(f"No puede lograrlo. Último destino: {ultimo_lugar}\nNecesitas {tiempo_restante} horas más para lograr el viaje ")
    

lugares1 = ["casa","montaña nevada","lago azul","valle verde"]
distancia1 = [0, 40, 100, 40]
tiempo_caminata1 = 40

lugares2 = ["casa","montaña nevada","lago azul","valle verde"]
distancia2 = [0, 40, 100, 40]
tiempo_caminata2 = 20

lugares3 = ["casa","duoc","mall","playa","cerro","playa con hueso de pollo","argentina"]
distancia3= [0,20,12,500,40,1000,4000]
tiempo_caminata3 = 100


aventurero(lugares3,distancia3,tiempo_caminata3)


        





print("Bienvenido al juego : Derríbame si puedes !")
from os import system
import time
cadena = "-----------"
vidas = 3
posicion_anterior=0
print("Tienes:" , vidas , "vidas")
while True:
    posicion_inicial=int(input("Ingrese una posición del 0 al 10: "))
    if posicion_inicial == 10 or posicion_inicial == 0:
        print("Te has caído de la cuerda :c")
        print("Intentalo otra vez !")
    else:
        break
posicion_j1=posicion_inicial
posicion_p=posicion_inicial
lista_cadena=list(cadena) #transforma la cadena a una lista de "-"
lista_cadena[posicion_inicial]="0" #reemplaza la posición inicial con un "0" en el lugar pedido
cadena_modificada="".join(lista_cadena) #une la lista a una cadena separada por "", en caso de querer probar otra separación ingresa el elemento que uno quiera
print (cadena_modificada)
cadena_modificada=cadena #regreso a la cadena original
while True: #me permite entrar a un bucle hasta que lo rompo con break
    print("La letra A te permite mover hacia la izquierda") #instrucciones de juego
    print("La letra D te permite permanecer en el centro")
    print("La letra S te permite mover hacia la derecha")
    jugador_1=input("Jugador 1 seleccione dirección (A), (S) ó (D): ").upper() #convierto a mayuscula para operar más facil, también pude haberlo hecho con minusculas
    if jugador_1 == "A": 
        posicion_anterior=posicion_j1 #almaceno la posicion anterior
        posicion_j1=posicion_inicial-1 #actualizo la posicion despues del comando ingresado
        system("cls") #se limpia el sistema
        break
    elif jugador_1 == "S":
        posicion_anterior=posicion_j1
        posicion_j1=posicion_inicial
        system("cls")
        break
    elif jugador_1 == "D":
        posicion_anterior=posicion_j1
        posicion_j1=posicion_inicial+1
        system("cls")
        break
    else:
        print("Comando no válido")
        time.sleep(1)
        system("cls")
while True: #me permite entrar a un bucle hasta que lo rompo con break
    print("La letra J te permite lanzar la piedra hacia la izquierda")
    print("La letra K te permite lanzar la piedra en el centro")
    print("La letra L te permite lanzar la piedra la derecha")
    jugador_2=input("Jugador 2 seleccione dirección (J), (K) ó (L): ").upper()
    if jugador_2 == "J":
        posicion_p=posicion_inicial-1
        system("cls")
        break
    elif jugador_2 == "K":
        posicion_p=posicion_inicial
        system("cls")
        break
    elif jugador_2 == "L":
        posicion_p=posicion_inicial+1
        system("cls")
        break
    else:
        print("Comando no válido")
        time.sleep(1) #da tiempo al jugador de ver que se equivocó al ingresar el comando
        system("cls")
if posicion_j1 == posicion_p:
    vidas = vidas - 1 #actualizo las vidas
    cadena_modificada=list(cadena_modificada)
    cadena_modificada[posicion_j1] = "0" #solo modifico 1 espacio para que no se sobreponga 0 con X
    cadena_modificada="".join(cadena_modificada)
else:
    cadena_modificada=list(cadena_modificada)
    cadena_modificada[posicion_j1] = "0"
    cadena_modificada[posicion_p] = "X"
    cadena_modificada="".join(cadena_modificada)
print(cadena_modificada)
if jugador_1 == "A":
    print("El Jugador 1 se ha movido hacia la Izquierda")
if jugador_1 == "S":
    print("El Jugador 1 se ha mantenido en el Centro")
if jugador_1 == "D":
    print("El Jugador 1 se ha movido hacia la Derecha")
if jugador_2 == "J":
    print("La piedra se ha lanzado a la Izquierda")
if jugador_2 == "K":
    print("La piedra se ha lanzado en el Centro")
if jugador_2 == "L":
    print("La piedra se ha lanzado a la derecha")
print("Tienes:" , vidas , "vidas")
cadena_modificada=cadena #vuelvo a la cadena original
while vidas != 0: #entro al bucle en torno a las vidas
    while True:
        jugador_1=input("Jugador 1 seleccione dirección (A), (S) ó (D): ").upper()
        if jugador_1 == "A": #me permite comparar números pasando las letras a ascii
            posicion_anterior=posicion_j1
            posicion_j1=posicion_anterior-1 #actualizo la posicion despues del comando ingresado
            system("cls") #se limpia el sistema
            break
        elif jugador_1 == "S":
            posicion_anterior=posicion_j1
            posicion_j1=posicion_anterior
            system("cls")
            break
        elif jugador_1 == "D":
            posicion_anterior=posicion_j1
            posicion_j1=posicion_anterior+1
            system("cls")
            break
        else:
            print("Comando no válido")
            time.sleep(1)
            system("cls")
    while True:
        jugador_2=input("Jugador 2 seleccione dirección (J), (K) ó (L): ").upper()
        if jugador_2 == "J":
            posicion_p=posicion_anterior-1
            system("cls")
            break
        elif jugador_2 == "K":
            posicion_p=posicion_anterior
            system("cls")
            break
        elif jugador_2 == "L":
            posicion_p=posicion_anterior+1
            system("cls")
            break
        else:
            print("Comando no válido")
            time.sleep(1)
            system("cls")
    if posicion_j1 == posicion_p:
        vidas = vidas - 1 #actualizo las vidas
        cadena_modificada=list(cadena_modificada)
        cadena_modificada[posicion_j1] = "0" #solo modifico 1 espacio para que no se sobreponga 0 con X
        cadena_modificada="".join(cadena_modificada)
    else:
        cadena_modificada=list(cadena_modificada)
        cadena_modificada[posicion_j1] = "0"
        cadena_modificada[posicion_p] = "X"
        cadena_modificada="".join(cadena_modificada)
    posicion_p=posicion_anterior
    print(cadena_modificada)
    if jugador_1 == "A":
        print("El Jugador 1 se ha movido hacia la Izquierda")
    if jugador_1 == "S":
        print("El Jugador 1 se ha mantenido en el Centro")
    if jugador_1 == "D":
        print("El Jugador 1 se ha movido hacia la Derecha")
    if jugador_2 == "J":
        print("La piedra se ha lanzado a la Izquierda")
    if jugador_2 == "K":
        print("La piedra se ha lanzado en el Centro")
    if jugador_2 == "L":
        print("La piedra se ha lanzado a la derecha")
    print("Tienes:" , vidas , "vidas")
    cadena_modificada=cadena
    if posicion_j1 == 0 or posicion_j1 == 10: #condicion de caida
        print("Te has caído de la cuerda :c ")
        print("Game Over")
        time.sleep(4)
        system("cls")
        break
    if vidas == 0:
        print("Te has quedado sin vidas :c ")
        print("Game Over")



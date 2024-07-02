#ejemplo Menu
#Puede copiar esto si estima conveniente

from autoHerramientas import *

#Con esto puede llamar a cualquier funcion creada en prueba.py
from prueba import *

#lista de autos
lista_autos = obtenerAutos("AutosBIG2")

opciones_menu = [
    "Opcion 1: Buscar auto por modelo",
    "Opcion 2: Imprimir lista de autos filtrados",
    "Opcion 3: Imprimir certificado",
    "Opcion 4: Buscar auto por patente",
    "Opcion 5: Buscar autos por rango de año",
    "Opción 6: Agregar información de dueño a un automóvil",
    "Opción 7: Muestra los autos de tu color favorito",
    "Opción 8: Buscar autos por nombre de propietario"
#agregar más opciones de forma similar
]

opciones_menu.append("Salir")

#COMANDOS INICIALES DE USUARIO

nombre_usuario = input("Ingrese su nombre: ").capitalize()
while True:
    print("***Ingrese la fecha actual***")
    dia_actual = input("Ingrese el día: ")
    mes_actual = input("Ingrese el mes: ")
    anno_actual = input("Ingrese el año: ")
    if (dia_actual.isdigit()) and (mes_actual.isdigit()) and (anno_actual.isdigit()):
        fecha_actual = dia_actual + "/" + mes_actual + "/" + anno_actual
        break
    else:
        print("Ingrese una fecha válida")
        continue
color_favorito = input("Ingrese su color favorito: ").capitalize()


while (True):
    #Mostrar Menu
    for i, opcion in enumerate(opciones_menu):
        print(i+1,". ",opcion, sep="")

    #Seleccionar
    while (True):
        seleccion = input("Ingrese una opción: ")
        if (validar_seleccion(seleccion,opciones_menu)):
            seleccion = int(seleccion)-1
            break
    
    #MOSTRAR OPCION --------------------
    print(opciones_menu[seleccion])


    #HACER ACCIONES ---------------------
    if (seleccion == 0):
        #opcion 1
        contador = 0
        modelo = input("Ingrese el modelo a buscar: ").title()
        for autos in lista_autos:
            if modelo in autos.values():
                contador = 1
                print(f"El modelo {modelo} pertenece a la marca {autos["marca"]} del año {autos["año"]} cuya patente es {autos["patente"]} y es de color {autos["color"]}")
        if contador == 0:
            print(f"El modelo {modelo} no se encuentra en nuestros archivos")
        pausa()
        limpiarPantalla()

    if (seleccion == 1):
        #opcion 2
        contador = 0
        llave = input("Ingrese una categoría (Modelo/Marca/Año/Patente/Color): ").lower()
        valor = input("Ingrese una característica de la categoría: ").capitalize()
        for autos in lista_autos:
            if (llave in autos.keys()) and (valor in autos.values()):
                    contador = 1
                    print(autos)
        if contador == 0:
            print("La categoría y la característica descritas no coinciden con nuestra base de datos")
        pausa()
        limpiarPantalla()

    if (seleccion == 2):
        for id,autos in enumerate(lista_autos):
            print(f"ID = {id+1} --- {autos}")
        id_seleccion = int(input("Ingrese el ID del vehículo que desea: "))
        vehiculo_elegido = lista_autos[id_seleccion-1]
        print(f"{nombre_usuario} emite certificado que:\nEl vehículo {vehiculo_elegido["marca"]} {vehiculo_elegido["modelo"]} con patente {vehiculo_elegido["patente"]}\nDe color {vehiculo_elegido["color"]}\nQueda registrado oficialmente a la fecha de {fecha_actual}")
        pausa()
        limpiarPantalla()

    if (seleccion == 3):
        contador = 0
        patente = input("Ingresa la patente del vehículo a buscar: ").upper()
        for autos in lista_autos:
            if patente == autos["patente"]:
                contador = 1
                print(autos)
        if contador == 0:
            print("La patente que buscas no se encuentra en nuestros archivos")
        pausa()
        limpiarPantalla()

    if (seleccion == 4):
        while True:
            rango1 = int(input("Ingrese el limite inferior del año a buscar: "))
            rango2 = int(input("Ingrese el límite superior del año a buscar: "))
            if rango2 < rango1:
                print("Rango de años mal ingresado")
                continue
            else:
                break
        print(f"El rango de búesqueda es entre los años {rango1} - {rango2}")
        for autos in lista_autos:
            if (rango1 < autos["año"]) and (rango2 > autos["año"]):
                print(autos)
        pausa()
        limpiarPantalla()

    if (seleccion == 5):
        for id,autos in enumerate(lista_autos):
            print(f"ID = {id+1} --- {autos}")
        id_seleccion = int(input("Ingrese el ID del vehículo que desea: "))
        vehiculo_elegido = lista_autos[id_seleccion-1]
        vehiculo_elegido.update({"nombre usuario":nombre_usuario})
        print(vehiculo_elegido)
        pausa()
        limpiarPantalla()

    if (seleccion == 6):
        for autos in lista_autos:
            if color_favorito in autos.values():
                print(autos)
        pausa()
        limpiarPantalla()

    if (seleccion == 7):
        #opcion 4
        pass

    if (seleccion == 8):
        print("Hasta pronto!")
        break

# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = ["Revisar menú",
        "Revisar carrito",
        "Pagar",
        "Quitar item de carrito",
        "Buscar item en carrito por nombre",
        "Buscar item en carrito por ingredientes",
        "Filtrar items que den alergia",
        "Burcar ítem",
        "Modificar ítem del menú",
        "Agregar ítem al menú",
        "Guardar carrito",
        "Cargar carrito",
        "Calcular calorías",
        "Salir"]

#Acciones iniciales


#menu principal
while (True):
    for i, opcion in enumerate(menu):
        print(f"{i+1}:{opcion}")
    
    while True:
        accion = int(input("Ingrese la acción a realizar: "))
        seleccion = menu[accion-1]
        break

    print(seleccion)

    if accion == 1:
        revisar_menu(var)
    if accion == 2:
        if carrito_user:
            print(carrito_user)
        else:
            print("El usuario no ha agregado comidas para comprar")

    if accion == 3:
        while True:
            ingrediente = input("Ingrese el ingrediente a buscar: ")
            buscar_ingrediente(var,ingrediente)
            opcion = input("Desea buscar otro ingrediente? (s/n): ")
            if opcion == "s":
                continue
            if opcion == "n":
                break
            
    if accion == 4:
        for i, elementos in enumerate(var):
            print(f"{i+1} , {elementos}\n")
        contra = input("Ingrese la contraseña: ")
        if check_password(contra):
            id = int(input("Ingrese el id del producto: "))
            sele = input("Ingrese que desea modificar (nombre,precio,kcal,ingredientes): ")
            producto = var[id-1]
            if sele in producto.keys():
                modi = input("Ingrese nuevo dato: ")
                producto[sele] = modi
        print(var)
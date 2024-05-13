inventario = []
print("***Inventario personal de objetos***")
while True:
    accion = input("Qué desea hacer? (Agregar/Reemplazar/Vaciar/Salir: ").lower()
    print(f"Mi lista actual de elementos en inventario es {inventario}") #muestra el inventario después de cada acción
    if accion not in "agregar,reemplazar,vaciar,salir": #condicion de acción no válida
        print("Ingrese una acción válida")
        continue
    elif accion == "agregar":
        if (len(inventario)) == 6: #condicion de capacidad máxima de almacenamiento
            print("Capacidad máxima de elementos almacenados, favor elegir otra opcion")
            continue #comando continue para que vuelva a preguntar que se desea hacer
        else:
            while True: #bucle para agregar elementos
                agregar_elemento = input("Ingrese el elemento a agregar: ")
                if not inventario: #si la lista está vacía entonces simplemente agregar el elemento
                    inventario.append(agregar_elemento)
                    break #salida del bucle de agregar elementos
                elif agregar_elemento in inventario: #condicion de duplicados, si se encuentra el elemento en la lista perdir que se agregue otro
                    print("No se admiten elementos duplicados, favor ingrese otra cosa")
                    continue #comando continue para volver a preguntar que elemento desea agregar
                else: #condicion de salida, si no se cumple nada de lo anterior, entonces que simplemente agregue el elemento
                    inventario.append(agregar_elemento)
                    break
    elif accion == "reemplazar": #accion de reemplazo
        reemplazar_elemento = input("Ingrese el elemento que desea reemplazar: ") #pregunto por el elemento a reemplazar
        reemplazar_2 = input("Qué elemento desea agregar en lugar del anterior?: ") #pregunto por el elemento que desea agregar a la lista
        inventario[inventario.index(reemplazar_elemento)] = reemplazar_2 #reemplazo el elemento anterior con el nuevo
        continue #comando continue para vuelva a preguntar que accion se desea realizar
    elif accion == "vaciar":
        inventario.clear() #comando clear() para vaciar la lista
        print("Se ha vaciado su inventario")
    elif accion == "salir": #condicion de salida
        break

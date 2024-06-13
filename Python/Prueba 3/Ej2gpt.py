lista_inventarios = []

def acepta_valores():
    global lista_inventarios #recurso de variable global
    dict_elemento = {}
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la candidad: "))
        precio = int(input("Ingrese precio: "))
        dict_elemento["nombre"] = nombre
        dict_elemento["cantidad"] = cantidad
        dict_elemento["precio"] = precio
        lista_inventarios.append(dict_elemento)
        eleccion = input("Desea agregar un nuevo elemento? si/no: ")
        if eleccion == "si":
            dict_elemento={}
            continue
        elif eleccion == "no":
            break
        else:
            print("Ingrese una opción válida")
            continue
    return lista_inventarios

def actualizar_articulo():
    global lista_inventarios
    nombre = input("Ingrese el nombre del artículo a modificar ")
    for elementos in lista_inventarios:
        if nombre in elementos.values():
            nueva_cantidad = int(input("Ingrese la nueva cantidad del elemento: "))
            elementos["cantidad"] = nueva_cantidad
        else:
            continue
    return lista_inventarios

def valor_total_inventario():
    global lista_inventarios
    lista_precios = []
    sumador = 0
    for elementos in lista_inventarios:
        precio = elementos.get("precio")
        cantidad = elementos.get("cantidad")
        total_elemento = precio * cantidad
        sumador += total_elemento

    return f"El valor total del inventario es {sumador}"

def articulos_mas_caros():
    global lista_inventarios
    lista_precios = []
    lista_mas_caros = []
    iteraciones = 0
    for elementos in lista_inventarios:
        iteraciones += 1
        precio = elementos.get("precio")
        lista_precios.append(precio)
    lista_precios.sort(reverse=True)
    for elementos in lista_inventarios:
        if lista_precios[0] in elementos.values():
            lista_mas_caros.append(elementos["nombre"])
        if lista_precios[1] in elementos.values():
            lista_mas_caros.append(elementos["nombre"])
        if lista_precios[2] in elementos.values():
            lista_mas_caros.append(elementos["nombre"])
    return f"Los elementos más caros son {lista_mas_caros[0]}  {lista_mas_caros[1]}  {lista_mas_caros[2]}"


acepta_valores()
print(articulos_mas_caros())

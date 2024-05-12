dict_llaves = {"(":")","{":"}","[":"]"}
finales = (")","}","]")
lista_aperturas = []
texto = input("Ingrese un texto: ")

for i in texto:
    if i in dict_llaves:
        lista_aperturas.append(i) #agrego las aperturas a una lista de aperturas
    elif i in finales:     
        if not lista_aperturas: #si la lista de caracteres está vacia significa que no se ha abierto ninguna llave
            print ("MAL ESCRITO")
            break
        ultima_llave = lista_aperturas.pop() #saco el ultimo elemento
        if dict_llaves[ultima_llave] != i: #comparo la llave del diccionario con su contenido, de ser distinto significa que no son correspondientes
            print("MAL ESCRITO")
            break
    if not lista_aperturas: #si la lista está vacía, significa que cada caracter se cerró correctamente
        print("BIEN ESCRITO")
        break
    else: #si la lista contiene algún caracter entonces no se cerró correctamente
        print("MAL ESCRITO")
        break

print(lista_aperturas)

#use diccionario porque así puedo comparar llaves con sus valores, por ejemplo si mi diccionario es dict = {"Comida":"Papapleto"} entonces puedo comparar 
# dict["comida"] == "Papapleto", en este caso retorna True ya que la llave corresponde con el valor
#para este caso comparo las aperturas con los cierres, si el ultimo cierre no corresponde con el valor de la ultima apertura entonces de inmediato imprimo False
#por defecto el booleano de una lista vacía es False, (print(bool(lista_app)) = False), por ende puedo verificar que una lista vacía sea True al poner not lista_vacia.
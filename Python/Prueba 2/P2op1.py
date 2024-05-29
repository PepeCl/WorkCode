#cree un programa que reciba 2 listas de string y devuelva lo siguiente
# 1.- una lista con todos los elementos que están en ambas listas OK
# 2.- todos los elementos que solo están en una lista OK 
# 3.- indicar que lista es más grande. el tamaño en este caso se considera como la suma de todas las vocales de la lista OK
# 4.- muestre en pantalla cuá es el elemento con más letras considerando ambas listas OK

def organizador_de_listas (lista1,lista2):
    lista_conjunta = []
    lista_unica = []
    contador_vocales_1=0
    contador_vocales_2=0
    contador_elemento=0
    vocales = "aeiou"

    for m in lista2:
        for n in m:
            if n.lower() in vocales:
                contador_vocales_2 += 1

    for i in lista1:
        for j in i:
            if j.lower() in vocales:
                contador_vocales_1 += 1
        if i in lista2:
            lista_conjunta.append(i)
            lista2.remove(i)
        elif i not in lista2:
            lista_unica.append(i)
        
    
    if contador_vocales_1 > contador_vocales_2:
        lista_mas_grande = "lista 1"
    elif contador_vocales_1 < contador_vocales_2:
        lista_mas_grande = "lista 2"
    
    lista_unica.extend(lista2)

    for i in lista_unica:
        if len(i) > contador_elemento:
            contador_elemento = (len(i))
            elemento_mas_grande = i

    return f"los elementos que se repite son: {lista_conjunta} \nlos elementos únicos son: {lista_unica}\nla lista más grande es la: {lista_mas_grande}\nel elemento más grande es: {elemento_mas_grande}"

lista_1 = ["abc","123","agb","1235","aaaaaaaAAAAAAAAAAAAAAAAAAA"]
lista_2 = ["123","hola","abc","1234","aaaaaaaaaaaaaaaaa"]

print(organizador_de_listas(lista_1,lista_2))

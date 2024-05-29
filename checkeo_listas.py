"""
Cree un programa que reciba 2 listas de strings y devuelva lo siguiente:

1- Una lista con todos los elementos que estan en AMBAS listas.
2- Todos los elementos que solo estan en UNA lista.
3- Indicar que lista es la mas "grande". El tamaño en este caso, se considera como la suma de todas las vocales de la lista.
4- Muestre en pantalla cual es el elemento con mas letras considerando AMBAS listas.
"""

lista_1 = []
lista_2 = []

print("Ingrese texto. Escriba 'salir' para terminar")

# Relleno para la lista 1
while True:
    elemento = input("Ingrese un texto para la lista 1: ")
    if elemento.lower() == "salir":
        break
    lista_1.append(elemento)

print("Ingrese un texto para la lista 2. 'salir' para terminar: ")
while True:
    elemento = input("Ingrese un texto para la lista 2: ")
    if elemento.lower() == "salir":
        break
    lista_2.append(elemento)

lista_1 = [elemento.strip() for elemento in lista_1] #Strip para enbellecer y borrar espacios en blanco al principio y fin que son inecesarios.
lista_2 = [elemento.strip() for elemento in lista_2]

elementos_comunes = [elemento for elemento in lista_1 if elemento in lista_2]  #para ver que elementos son comunes

elementos_unicos = [elemento for elemento in lista_1 + lista_2 if elemento not in elementos_comunes] # Para ver los elementos unicos de cada lista

total_vocales_l1 = sum(elemento.lower().count(vocal) for elemento in lista_1 for vocal in "aeiou") #count para contar las vocales de cada elemento de la lista 1

total_vocales_l2 = sum(elemento.lower().count(vocal) for elemento in lista_2 for vocal in "aeiou")

# Condiciones para saner que lista es mas grande o si tienen el mismo tamaño
if total_vocales_l1 > total_vocales_l2:
    mas_grande = "La primera lista es la mas grande."
elif total_vocales_l1 < total_vocales_l2:
    mas_grande = "La segunda lista es la mas grande."
else:
    mas_grande = "Ambas listas tienen el mismo tamaño."

# Ciclo para saber cual es el elemento mas largo y con mayor longitud
mas_largo = ""
max_longitud = 0

for elemento in lista_1 + lista_2:
    if len(elemento) > max_longitud:
        mas_largo = elemento
        max_longitud = len(elemento)


print("1- Elementos en ambas listas:", elementos_comunes)
print("2- Elementos únicos en una lista:", elementos_unicos)
print("3- Lista más grande:", mas_grande)
print("4- Elemento más largo en ambas listas:", mas_largo)
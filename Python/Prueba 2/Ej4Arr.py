lista_numeros = []
lista_eliminar = []
while True:
    numeros = float(input("Ingrese cualquier número: "))
    if numeros == 0:
        break
    else:
        lista_numeros.append(numeros)
print(lista_numeros)
eliminar_numeros = float(input("Ingresa otro número: "))
for i in lista_numeros:
    if (i < eliminar_numeros):
        lista_eliminar.append(i)
for j in lista_eliminar:
    lista_numeros.remove(j)
print(lista_numeros)
lista = []
for i in range (20):
    lista.append(i)
lista.insert(0,100)
print(lista)

ultimo = lista.pop(0)

print(lista)
print(ultimo)
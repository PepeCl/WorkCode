import random
contador = 10
lista_numeros = []
while contador != 0:
    aleatorio = random.randint(1,100)
    lista_numeros.append(aleatorio)
    print(aleatorio)
    contador -= 1

print(lista_numeros)
print(lista_numeros[1])
print(lista_numeros[5])


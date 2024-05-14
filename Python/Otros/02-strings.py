lista_prueba = ["abcs","zxcv"]
abecedario = list("abcdefghijklmnopqrstuvwxyz")
lista_suma =[]
sumador = 0
for i in lista_prueba:
    for j in i:
        if j in abecedario:
            sumador += (abecedario.index(j)+1)
    lista_suma.append(sumador)
    sumador = 0
print(lista_suma)
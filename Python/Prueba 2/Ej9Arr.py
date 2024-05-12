lista_numeros = [1,2,3,4,5,6,7,2,3,4,5,6,1,2,4,5,7,8,9,12,12,13,10,1,0,0,0,0,5,2]
lista_rep = []
for i in lista_numeros:
    if i in lista_rep:
        continue
    else:
        lista_rep.append(i)
    print(f"el numero {i} se repite {lista_numeros.count(i)} veces")


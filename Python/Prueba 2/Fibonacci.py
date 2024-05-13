numero = int(input("Ingrese un número cualquiera: "))
sumador_1 = 1
sumador_2 = 0
sumador_3 = 0 
lista = [0] #como el primer número de fibonacci es 0, entonces agrego ese valor por default
print("La secuencia fibonacci para tu numero es:")
for i in range (numero):
    sumador_3=sumador_2+sumador_1 #creo una variable de suma final
    sumador_1=sumador_2 #actualizo la variable 2 en la variable 1
    sumador_2=sumador_3 #actualizo la variable 3 en la variable 2, así guardo la suma y actualizo las variables para volver a sumarlas más adelante
    if sumador_3 > numero: #contición de que si la suma final es mayor al número ingresado entonces NO agregue la respuesta a la lista. de no agregar esta condición, iteraría el número de veces ingresado, es decir si ingreso 40 haría 40 iteraciones
        break 
    lista.append(sumador_3) #agrego al final de la lista la suma en cada iteración

print(lista)


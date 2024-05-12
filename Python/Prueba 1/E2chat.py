numero = int(input("Ingrese un número: "))
for i in range (2,numero):
    if numero % i == 0:
        print("No es primo")
        print(numero % i)
        break
    else:
        es_primo=True
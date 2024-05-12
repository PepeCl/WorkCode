numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("número inválido")
contador=0
for i in range (1,numero+1):
    if numero % i == 0:
        contador = contador + i
    
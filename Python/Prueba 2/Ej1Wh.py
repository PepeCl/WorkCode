suma = 0
cont = 0
while True:
    numero=input("Ingrese un número: ")
    if numero == "salir":
        break
    else:
        suma = int(numero) + suma
        cont = cont + 1
print(suma)
print(suma/cont)


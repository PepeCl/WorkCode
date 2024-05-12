contador = 0
suma = 0
while True:
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    contador += 1
    if suma >= 20:
        break
    elif contador == 10:
        print(f"Se acepta un máximo de {contador} números")
        break
print(f"La suma total es de {suma}")
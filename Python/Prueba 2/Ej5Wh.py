mayor = 0
menor = 0
contador = 0
while True:
    numero = input("Ingrese un número: ")
    contador += 1
    if numero.isalpha() == True:
        print("Elemento no válido, ingrese un número")
        continue
    if int(numero)  == 0:
        break
    if contador == 1:
        numero = int(numero)
        mayor = numero
        menor = numero
        continue
    if contador > 1:
        if int(numero) > mayor:
                mayor = int(numero)
        elif int(numero) < menor:
                menor = int(numero)
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")



            



lista = []
a=0
while True:
    numero = input("Ingrese un número entero: ")
    if numero == "salir":
        break
    lista.append(int(numero))
for i in lista:
    if i > a:
        a = i
print(a)
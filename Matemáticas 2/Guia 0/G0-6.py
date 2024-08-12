def multiplicador(n1,n2):
    return n1*n2

print(multiplicador(2.2,3.2))

def redondear_entero(numero):
    return int(numero)

print(redondear_entero(multiplicador(2.2,3.3)))

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

producto = multiplicador(numero_1,numero_2)

print(producto)
print(redondear_entero(producto))
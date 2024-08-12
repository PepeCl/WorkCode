numero = int(input("Ingrese un número: "))

for multiplicador in range (1,13):
    respuesta = multiplicador * numero
    print(f"{numero} * {multiplicador} = {respuesta}")
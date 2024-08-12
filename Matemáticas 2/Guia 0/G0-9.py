def imc(peso,altura):
    indice = (peso/(altura**2))
    return indice
"""
peso = float(input("Ingrese su peso en [Kg]: "))
altura = float(input("Ingrese su altura en [m]: "))

persona = imc(peso,altura)

if persona < 18.5:
    print("Su condición es BAJO PESO")
elif ((persona >= 18.5) and (persona < 24.9)):
    print("Su condición es Peso Normal")
elif (persona >= 25) and (persona < 29.9):
    print("Su condición es SOBREPESO")
elif persona > 30:
    print("Su condición es OBESO")"""

lista_imc = [16.43,19.31,10.25,18.63,17.85,19.76,23.64,21.94,21.3,22.67,16.48]

for numero,persona in enumerate(lista_imc):
    if persona < 18.5:
        print(f"La persona N°{numero+1} se encuentra BAJO PESO")
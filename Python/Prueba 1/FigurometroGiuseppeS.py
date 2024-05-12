import math
import time
from os import system
print("Puedo calcular el área de las siguientes figuras: Circulo, Rectángulo, Elipse, Hexágono y Triángulo.")
figura = input("De qué figura desea calcular el área?: ").lower()
if figura == "triangulo":
    while True: #entro a un bucle para cuando el usuario ingresa valores no válidos, asi el programa no termina y sigue preguntando valores
        base=float(input("Ingrese la medida de la base en [m]: "))
        altura=float(input("Ingrese la medida de la altura en [m]: "))
        if base < 0 or altura < 0:
            print("Has ingresado algún valor negativo, por favor ingrese un número válido")
            time.sleep(1.5) #el programa muestra durante 1.5 segundos el mensaje en pantalla
            system("cls") #se limpia la pantalla para más orden visual
        else:
            area=(base * altura)/2
            print("El área del Triángulo es:" , area , "[m^2]")
            break #luego de cumplida la condicion, se sale del bucle para no preguntar más veces el valor de los lados
elif figura == "rectangulo":
    while True:
        base=float(input("Ingrese la medida de la base en [m]: "))
        altura=float(input("Ingrese la medida de la altura en [m]: "))
        if base < 0 or altura < 0:
            print("Has ingresado algún valor negativo, por favor ingrese un número válido")
            time.sleep(1.5)
            system("cls")
        elif base == altura:
            print("Tu rectagulo es un CUADRADO !")
            area = base * altura
            print("El área del Cuadrado es:", area, "[m^2]")
            break
        else:
            area = base * altura
            print("El área del Rectángulo es:" , area ,"[m^2]")
            break
elif figura == "circulo":
    while True:
        radio=float(input("Ingrese la medida del radio en [m]: "))
        if radio < 0:
            print("Has ingresado algún valor negativo, por favor ingrese un número válido")
            time.sleep(1.5)
            system("cls")
        else:
            area = (radio**2)*math.pi #importe el valor de pi desde la biblioteca math para más precisión
            print("El área del Circulo es:",area,"[m^2]")
            break
elif figura == "elipse":
    while True:
        radio1=float(input("Ingrese la medida del primer radio en [m]: "))
        radio2=float(input("Ingrese el valor del segundo radio en [m]: "))
        if radio1 < 0 or radio2 <0:
            print("Has ingresado algún valor negativo, por favor ingrese un número válido")
            time.sleep(1.5)
            system("cls")
        elif radio1 == radio2:
            print("Tu elipse es un CIRCULO !")
            area = (radio1**2)*math.pi
            print("El área del Circulo es:",area,"[m^2]")
            break
        else:
            area = radio1*radio2*math.pi
            print("El área del Elipse es:",area,"[m^2]")
            break
elif figura == "hexagono":
    while True:
        lado=float(input("Ingrese la medida de uno de los lados en [m]: "))
        apotema=float(input("Ingrese el valor del apotema en [m]: "))
        if lado < 0 or apotema < 0:
            print("Has ingresado algún valor negativo, por favor ingrese un número válido")
            time.sleep(1.5)
            system("cls")
        else:
            area = ((lado*6)*apotema)/2
            print("El área del Hexágono es:",area,"[m^2]")
            break
else:
    print("No se calcular esa figura :c")
    time.sleep(1.5)
    system("cls")

            
        

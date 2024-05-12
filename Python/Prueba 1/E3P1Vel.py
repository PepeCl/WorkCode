print("Programa de multas por exceso de velocidad :o ")
velocidad_registrada = float(input("Ingrese la velocidad del auto en cuestión: "))
limite_velocidad=float(input("Ingrese el límite de velocidad de su ciudad: "))
exceso=((velocidad_registrada-limite_velocidad)/limite_velocidad)*100
velocidad=velocidad_registrada-limite_velocidad
if exceso == 0:
    print("Su infracción es de $",0 )
elif 0 < exceso <= 15:
    print("Su infracción es de $", 10*velocidad)
elif 16 < exceso <=25:
    print("Su infracción es de $", 40*velocidad)
elif 26 < exceso <=50:
    print("Su infracción es de $", 4000+int(15*velocidad))
else:
    print("Su infracción es de $", 10000+int(30*velocidad))




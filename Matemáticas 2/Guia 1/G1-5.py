import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def distancia_en_metro(tiempo):
    return (0.4 * tiempo) - 6

def distancia_en_bus(tiempo):
    return (0.3 * tiempo) - 6
"""
tiempo = np.arange(0,10,0.1)
dist_metro = 0.4 * tiempo
dist_bus = 0.3 * tiempo

plt.plot(tiempo,dist_metro)
plt.plot(tiempo,dist_bus)

plt.xlabel("Tiempo [seg]")
plt.ylabel("Distancia recorrida [Km]")
plt.grid(True)

plt.show()
"""

#se asume que la persona toma el metro en cuanto llega el tren a la estacion y se baja en cuanto el tren llega a la estacion.
estaciones = 9
lista_dominio = []
for iteracion in range (estaciones):
    if iteracion == 8:
        dominio = 1.2 + dominio
    else:
        dominio = 1.2 * iteracion + 0.5 * (iteracion+1)
    lista_dominio.append(dominio)
print(f"El dominio de la funcion es {lista_dominio}")

""" Mediante análisis gráfico se puede determinar que en metro se recorre más distancia que en micro en el mismo tiempo."""

metro = fsolve(distancia_en_metro,6)
bus = fsolve(distancia_en_bus,6)

print(f"Si la distancia son 6 [Km] entonces en metro se demora {metro} [min]")
print(f"Si la distancia son 6 [Km] entonces en bus se demora {bus} [min]")
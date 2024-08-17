#1562 elementos, 7 horas de trabajo
#a(n) = 0.01n**2+0.5n+2
#n = elementos a ordenar, a(n) tiempo en segundos

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fsolve

"""La variable independiente son los elementos a ordenar [unidades] y la variable dependiente es el tiempo [seg]"""
"""El dominio son todos los naturales comprendidos entre el 0 y 1562"""

def ordenar_elementos(elementos):
    tiempo = 0.01 * (elementos ** 2) + (0.5 * elementos) +2
    return tiempo

def buscar_respuesta(elementos):
    return 0.01 * (elementos ** 2) + (0.5 * elementos) + 2 - 21600


elementos = np.arange(0,1562,1)
tiempo = ordenar_elementos(elementos)
plt.plot(elementos,tiempo)
plt.xlabel("Elementos [Unidades]")
plt.ylabel("Tiempo [seg]")
plt.grid(True)
plt.show()

print(ordenar_elementos(1200))
print(fsolve(buscar_respuesta,21600))

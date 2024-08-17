import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fsolve
import math

def tiempo_ejecucion_buscar(elementos):
    return elementos * 0.02 - 50


elementos = np.array([100,200,500,1000,2000])
tiempo = np.array([2,4,10,20,40])
pendiente, interseccion = np.polyfit(elementos,tiempo,1)
print(round(pendiente,3))
print(round(interseccion,3))

elementos_funcion_tiempo = 1500 / 0.02

plt.plot(elementos,tiempo)
plt.grid(True)
plt.show()

print(f"para 1500 elementos el tiempo que demora es {elementos_funcion_tiempo} [ms]")
print(f"El tamaño de entrada para obtener un tiempo de 50 [ms] es {fsolve(tiempo_ejecucion_buscar,50)} elementos")
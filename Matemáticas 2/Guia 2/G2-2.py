import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fsolve
import math

""" La variable independiente es el volúmen de datos [Gb] y la variable dependiente es el tiempo [min]"""

volumen = np.array([5,10,25,50,100])
tiempo = np.array([10,20,50,100,200])
m,n = np.polyfit(volumen,tiempo,1)
print(f"La pendiente de la función es {round(m,3)} y la intersección con el eje Y es {round(n,3)}")
plt.plot(volumen,tiempo)
plt.grid(True)
plt.show()

"""La funcion que modela el problema es y = 2x """
"""La pendiente quiere decir que por cada Gb de dato transferido pasan 2 minutos"""

def buscar_volumen(elementos):
    return (elementos * 2) - 123.5

print(f"El volúmen de datos en [Gb] que son transferidos luego de 124.5 [min] son {fsolve(buscar_volumen,123.5)}")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import math

"""La variable independiente es el tiempo [meses] y la variable dependiente son los usuarios [unidades]"""

def funcion_red_social(tiempo):
    usuarios = (1000) / (1+(9*np.exp((-0.5) * tiempo)))
    return usuarios

def determinar_tiempo(tiempo):
    return ((1000) / (1+(9*math.exp((-0.5) * tiempo)))) - 800

caso_1 = funcion_red_social(12)
print(f"Tras 12 meses los usuarios en la red social es {int(caso_1)} personas") #aproximamos al entero para dato más real

"""tiempo = np.arange(0,24,1)

plt.plot(tiempo,funcion_red_social(tiempo))
plt.xlabel("Tiempo en meses")
plt.ylabel("Usuarios")
plt.grid(True)
plt.show()"""

usuarios = fsolve(determinar_tiempo,800)
print(usuarios)
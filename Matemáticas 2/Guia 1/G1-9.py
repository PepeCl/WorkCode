#consumo de energia de datacenter e(t) = 50 * log (t+1) + 200
#t tiempo en horas

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fsolve
import math


"""La variable independiente es el tiempo [horas] y la variable dependiente es la energia [kWh]"""

def consumo_energia(tiempo):
    energia = 50 * np.log10 (tiempo + 1) + 200
    return energia

def buscar_consumo(tiempo):
    return 50 * np.log10 (tiempo + 1) - 150

print(f"En 5 Horas se consumen {consumo_energia(5)} [kWh]")

tiempo = np.arange(0,1000,0.1)
energia = consumo_energia(tiempo)
plt.plot(tiempo,energia)
plt.xlabel("Tiempo [seg]")
plt.ylabel("Consumo energía [kWh]")
plt.grid(True)
plt.show()

"""Para consumir 350 [kWh] deben transcurrir 999 horas"""

print(fsolve(buscar_consumo,350))
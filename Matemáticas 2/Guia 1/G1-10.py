#carga de trabajo en funcion del tiempo W(t) = 100 * e ^ (-0.1 * t)
#tiempo en semanas

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fsolve
import math

def calculo_porcentaje_trabajo(tiempo):
    trabajo = 100 * np.exp(-0.1 * tiempo)
    return trabajo

def obtener_semanas(tiempo):
    return ((100 * np.exp(-0.1 * tiempo)) - 55)    

print(calculo_porcentaje_trabajo(12))
print(fsolve(obtener_semanas,55))